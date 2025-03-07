import pandas as pd

raw = pd.read_csv("http://hilpisch.com/pyalgo_eikon_eod_data.csv",
                  index_col=0, parse_dates=True).dropna()
# print(raw.head())
# print(raw.columns)
raw.rename(columns={"AAPL.O": "AAPL"}, inplace=True)
df = pd.DataFrame(raw["AAPL"])
print(df.tail())
