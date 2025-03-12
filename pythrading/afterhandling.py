from pandas import Series, DataFrame

data = [100,200,300,400,500,600,700,800,900,1000]
second_index = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

data = Series(data, index=second_index)

# print(data[data.values > 500])

data = {
    "open": [737, 750],
    "high": [750, 760],
    "low": [730, 740],
    "close": [740, 750],
}

df = DataFrame(data, index=["2025-03-11", "2025-03-12"])
df["volatility"] = df["high"] - df["low"]
print(df)