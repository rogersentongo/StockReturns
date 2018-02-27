import pandas as pd
import numpy as np
import pandas_datareader.data as web
import quandl
from datetime import datetime, timedelta
quandl.ApiConfig.api_key= 'Insert API Key here'



def get_stockdata():
        #Creates a dataframe from the constituents csv file
        newlist = pd.read_csv('constituents.csv')

        #Creates a series containing the tickers for each stock
        newerlist = pd.Series(newlist['Symbol'])

        #Creates a list of 500 stock tickers
        newestlist = newerlist.tolist()

        #An empty list to store the tickers
        Stock_tickers = []

        #We create a list of 500 wiki strings
        wikilist = []
        for i in range(80):
            wikilist.append('WIKI/')

        #For loop to append ticker name to string
        for i in range(80):

            #Creates a new ticker e.g WIKI/AAPL
            name = wikilist[i] + newestlist[i]

            #Appends new ticker to list
            Stock_tickers.append(name)

        #note!! I readjusted the tickers below from the constituents.csv file to brb_b from brb.b
        #print(Stock_tickers[66])
        #print(Stock_tickers[77])

        #Create a list of adj.close tickers
        adjclose=[]
        AdjClose_tickers = []
        for i in range(80):
            adjclose.append('.11')

        for i in range(80):
            name = Stock_tickers[i] + adjclose[i]

            #New ticker list containing .11 for adj close column
            AdjClose_tickers.append(name)


        #Creates a date object showing today's date with extra data
        now = datetime.now()
        Thirty_now = now - timedelta(30)
        Thirty_now = Thirty_now.strftime('%Y-%m-%d')


        #Create a date_now string object that only includes the year month and day
        Date_now = now.strftime('%Y-%m-%d')
        #print(Date_now)
        #print(Thirty_now)



        data = quandl.get(AdjClose_tickers, start_date=Thirty_now, end_date=Date_now, order='asc')

        data.to_csv('30DayStocks.csv')
        return
