import pandas as pd

student_total = {"s1":450,"s2":475,"s3":490,"s4":485}

series = pd.Series(student_total)

print(series["s3"])

# convert a employee dictionary and convert that to series

employee = {"Abin":60000,"Shajeer":62000,"Lijo":61000,"Shafi":63000}

series = pd.Series(employee)

print(series["Shajeer"])

print("Total ",series.sum())
print("Max",series.max())
print("Min",series.min())
print("Average",series.mean())