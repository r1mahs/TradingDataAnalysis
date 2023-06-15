# TradingDataAnalysis
This is a repo of a personal project of mine where I wanted to simulate, analyze and visualize a trading firms data.

First I needed to simulate trading data, to get an idea of what the data would look like I reached out to a business connection who is a head at a top cryptocurrency trading firm.

He told me that for this project it would make sense for me to format the data into a .csv with 3 collumns, 'userid', 'tradevalue' and 'tradedate'. Obviously there is more data that could be used, but
for this project sake I worked with this becuase it would form a solid base to continue from.

From there then I went to python to write a script that would generate the data. A similar script I used can be found in the 'Generate_Data.py' python file. 

Then to simulate the environment of a trading firm I converted the csv into a database and uploaded it to MySQL Workbench 8.0.

From there, the data was analyzed in SQL.

Three important metrics that I was told are constantly looked at are, 
  1) Average Monthly Volatility - This is important because it gives an understanding of when the market is most volatile, and risk should be accessed conservatively.
  2) User Average Networth - This is important because it allows you to track which users are trading the most money on your firm, something that should be constantly tracked.
  3) Average Trades per Month - This is important becaue it is a metric that allows you to see the usage of the Firm m/m.

From there I wrote SQL queries to find out this information which can be found in the 'SQL_Queiries' section.

(Note: Since the data was randomly generated, it may all looks pretty similar which makes sense because normal distribution).

Lastly, I wanted to show off this information using Power BI, which can be found in the 'Power_BI_Visualization' section.
