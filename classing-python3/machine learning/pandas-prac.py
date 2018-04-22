import pandas as pd
import numpy


class container:
    class workArea:
        master=None

    class data:
        master=None
        countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan','delvin']
        gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0,0]
        silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0,0]
        bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1,0]

    class processing:
        master=None
        def generateSeries(self,gold,silver,bronze,countries):
            seriesTotal={'bronze':pd.Series(bronze),'country_name':pd.Series(countries),'gold':pd.Series(gold),'silver':pd.Series(silver)}
            return seriesTotal
        def generateDF(self,series):
            return pd.DataFrame(series)
        
        def filterAZM(self,df):
            a=df['country_name'][df['bronze'] < 1].tolist()
            b=df['country_name'][df['silver'] < 1].tolist()
            c=df['country_name'][df['gold'] < 1].tolist()
            az=[]
            az.extend(a)
            az.extend(b)
            az.extend(c)
            az.sort()
            azFinal=[]
            for country in az:
                if country not in azFinal:
                    azFinal.append(country)
            zscore=[]
            for i in azFinal:
                if i in a:
                    if i in b:
                        if i in c:
                            zscore.append(i)
            for i in zscore:    
                df=df[df.country_name != i]
            return df

        def totalPoints(self,filterDF):
            totals=numpy.dot(filterDF[['gold','silver','bronze']],[4,2,1])
            countries=filterDF.country_name
            newSeries={'country_name':pd.Series(countries),'points':pd.Series(totals)}
            newDF=pd.DataFrame(newSeries)
            return newDF

    class display:
        master=None
        def display(self,data):
            print(data)

    def assembler(self):
        wa=self.workArea()
        
        wa.data=self.data()
        wa.data.master=wa
        
        wa.dfs=self.processing()
        wa.dfs.master=wa
        
        wa.display=self.display()
        wa.display.master=wa

        wa.series=wa.dfs.generateSeries(
                wa.data.gold,
                wa.data.silver,
                wa.data.bronze,
                wa.data.countries)
        
        wa.df=wa.dfs.generateDF(wa.series)
        #display country, gold medal
        '''wa.display.display(wa.df[['country_name','gold']])'''
        #display by row
        '''wa.display.display(wa.df.loc[25])'''
        #display all
        '''wa.display.display(wa.df)'''
        #useful stats
        '''wa.display.display(wa.df.describe())'''
        #conditionally get rows
        '''wa.display.display(wa.df[wa.df['gold'] >= 5])'''
        #conditionally get col from rows
        '''wa.display.display(wa.df['country_name'][wa.df['gold'] >= 5])'''
        #using numpy on df
        '''wa.display.display(wa.df[['gold','silver','bronze']].apply(numpy.average))'''
        #data frame map column
        '''wa.display.display(wa.df['country_name'][wa.df['bronze'].map(lambda x: x <= 5)])'''
        '''wa.display.display(wa.df[['bronze','gold','silver']].applymap(lambda x: x <= 5))'''
        '''wa.display.display(wa.df.applymap(lambda x: x <= 5 if type(x) != type('') else x))'''
        '''wa.display.display(wa.df[['gold','silver','bronze']].apply(numpy.mean))'''
        #get average of all medals earned for any country that had atleast one medal in [silver,gold,bronze]
        '''wa.display.display(wa.df[wa.df['silver'] >= 1][wa.df['gold'] >=1][wa.df['bronze'] >=1][['silver','gold','bronze']].apply(numpy.mean))'''
        filterDF=wa.dfs.filterAZM(wa.df)
        totalPoints=wa.dfs.totalPoints(filterDF)
        print(totalPoints)

run=container()
run.assembler()
