import pandas as pd
import datetime
import yfinance as yf

# Define the symbol for NIFTY Bank index
symbol = "^NSEBANK"

# Define the start and end dates for the historical data
start_date = datetime.date(2015, 1, 1)
end_date = datetime.datetime.today()

# Fetch historical data using yfinance
data = yf.download(symbol, start=start_date, end=end_date)

# Round the data to two decimal places
data = round(data, 2)

# Select specific columns: "Open", "High", "Low", "Close", and "Volume"
data = data[["Open", "High", "Low", "Close", "Volume"]]

# Display information about the DataFrame using info()
print(data.info())

# Save the DataFrame to a CSV file named "BankNifty_Data.csv"
data.to_csv("BankNifty_Data.csv")

# Optionally, you can display the first few rows of the DataFrame
print(data.head())
