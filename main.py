import pandas as pd
import numpy as np
import pandas_datareader.data as web
import quandl
from datetime import datetime, timedelta
import stockdata

#Creates an updated list of stocks
stockdata.get_stockdata()


#Creates a dataframe from the constituents csv file
prices = pd.read_csv('30DayStocks.csv')

#Set the index to the Date
prices2 = prices.set_index('Date')



#We get no. of index columns so that we can use them for calculating the periods parameter for pct_change
index_no = len(prices2.index)
print(index_no)


# print('THE CODE BELOW HAS THE DAILY RETURNS')
# print(prices2.pct_change())

#print('THE CODE BELOW HAS THE 30 DAY RETURNS')
#Although there are 21 days with percent returns we need to use 20 periods because last day has no return
perc_change30 = prices2.pct_change(periods=index_no-1)*100


#We're going to use iloc because it selects a row by integer position of an index
#Additionally, we're going to subtract one from the length of the index because its a 0 based index when using iloc

final_returns = pd.DataFrame(perc_change30.iloc[index_no-1])
#We use reset_index function in order to make the ticker names a column
final_returns = final_returns.reset_index()
#We use the .rename function to rename the index column to Ticker
final_returns = final_returns.rename(columns={'index': 'Ticker'})


#We need to find last dateindex value
date_index_list = prices2.index.values
last_index_value = date_index_list[index_no-1]

final_returns = final_returns.sort_values(by=last_index_value, ascending=False)



#We need to sort the columns
print(final_returns)

#We need to get the top 30 and the bottom thirty
Top30 = final_returns.head(30)
Bottom30 = final_returns.tail(30)

print("These are the top 30 stocks based off thirty day returns".upper())
print(Top30.reset_index(drop=True))


print()
print()
print("These are the bottom 30 stocks based off thirty day returns".upper())
print(Bottom30.reset_index(drop=True))
