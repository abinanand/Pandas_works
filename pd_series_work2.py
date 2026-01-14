import pandas as pd

data = [68,70,69,75,63,55,65,71,82,90]

series = pd.Series(data)
print(series)


# head() list first 5 records
# tail() list last 5 records

print(series.head())
print(series.tail())


print(series.shape)