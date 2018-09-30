#! /usr/bin/env python3

import urllib.request
import json
import numpy as np

class getproducts:
    master=None
    fieldsTop=['itemId', 'parentItemId',
            'name', 'salePrice',
            'upc', 'categoryPath',
            'shortDescription',
            'longDescription', 'brandName',
            'thumbnailImage','productTrackingUrl',
            'ninetySevenCentShipping', 'standardShipRate',
            'size', 'color', 'marketplace',
            'shipToStore', 'freeShipToStore', 
            'modelNumber', 'productUrl','categoryNode',
            'bundle', 'clearance', 'preOrder', 'stock',
            'addToCartUrl', 'affiliateAddToCartUrl', 
            'freeShippingOver50Dollars', 'giftOptions', 
            'offerType', 'isTwoDayShippingEligible', 
            'availableOnline','attributes']
    giftOp=['allowGiftWrap','allowGiftMessage',
            'allowGiftReceipt']
    attr=['color','replenishmentEndDate',
            'size']
    apikey=''

    baseUrl='http://api.walmartlabs.com/v1/items?apiKey={}&format=json&upc={}'
    url=''

    def initFields(self):
        data={}
        apikey=self.apikey
        for i in self.fieldsTop:
            if i == 'giftOptions':
                for sub_i in self.giftOp:
                    data['{}_{}'.format(i,sub_i)]=''
            elif i == 'attributes':
                for sub_i in self.attr:
                    data['{}_{}'.format(i,sub_i)]=''
            elif i == 'thumbnailImage':
                data[i]=np.zeros((40,40,3), np.uint8)
            else:
                data[i]=''
        return data

    def adjustUrl(self,apikey,upc):
        self.url=self.baseUrl.format(apikey,upc)

    def getData(self):
        data=urllib.request.urlopen(self.url)
        return data
    def getThumbnail(self,url):
        uri=urllib.request.urlopen(url)
        data=uri.read()
        return data

    def loadData(self,data):
        data=json.load(data)
        return data['items'][0]

    def flattenData(self,upc):
        data={}
        apikey=self.apikey
        self.adjustUrl(apikey,upc)
        try:
            raw=self.getData()
            raw=self.loadData(raw)
            for i in self.fieldsTop:
                if i == 'giftOptions':
                    for sub_i in self.giftOp:
                        if sub_i in [x for x in raw[i].keys()]:
                            data['{}_{}'.format(i,sub_i)]=raw[i][sub_i]
                elif i == 'attributes':
                    for sub_i in self.attr:
                        if sub_i in [x for x in raw[i].keys()]:
                            data['{}_{}'.format(i,sub_i)]=raw[i][sub_i]
                elif i == "thumbnailImage":
                        data[i]=self.getThumbnail(raw[i])
                else:
                    data[i]=raw[i]
        except OSError as e:
            print(e)
            print("404: {}".format(self.url))
        return data

