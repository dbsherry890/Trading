import mplfinance as mpf
from datetime import datetime, timedelta
import pandas as pd
import yfinance as yf
# import mplfinance as mpf
from datetime import datetime, timedelta

# ticker_symbol = 'AAPL'

# data = yf.download(ticker_symbol, start='2020-01-01', end='2023-01-01')
# print(data)

# weekly_data = yf.download("AAPL", start="2025-01-10",
#                           end="2025-01-11", interval="15m")
# print(weekly_data)

goog = yf.Ticker("GOOG")
print(goog.history(period="1d"))
