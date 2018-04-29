#! /usr/bin/env bash

#get product information from walmart api using upc (barcode)
apikey="$1"
format="json"
barCode="$2"

url="http://api.walmartlabs.com/v1/items?apiKey=$apikey&format=$format&upc=$barCode"
echo "$url"
