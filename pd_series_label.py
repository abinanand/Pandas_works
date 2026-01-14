import pandas as pd

salary = [30000,32000,35000,45000,55000]

series = pd.Series(salary)

print(series[1])
print(series[0])
print(series[2:4])

series = pd.Series(salary, index = ["e1","e2","e3","e4","e5"])

print(series["e3"])
print(series["e1":"e4"])