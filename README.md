# StockReturns
A program that returns 30 day stock returns of the top and bottom 30 stocks in the S&P 500.

**To run the program, run the main.py file.**

Modules used: Pandas, Quandl, Numpy, Pandas-datareader

## How it Works:
1.) The *constituents.csv* file contains a list of stock ticker names for the S&P 500 index.

2.) The **stockdata.py** file contains a function that loads the ticker names from the *constituents.csv* file. It then uses the quandl module
    to get stock proces for 80 of the stocks. This data is loaded into the *30DayStocks.csv* file.

3.) The **main.py** file starts by loading the function in the stockdata.py file. This is done in order to refresh the stock data. After this,
    the program uses the pandas and numpy libraries to calculate the thirty day returns for each indivual stock and then returns a list of
    the top and bottom 30 performing stocks based on their 30 day returns.

Note: Users can modify the stockdata.py file to take in more stock data up to 505 stocks(Uses a zero based index for 506 stocks).


