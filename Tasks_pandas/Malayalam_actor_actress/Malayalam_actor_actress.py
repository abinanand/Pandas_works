import pandas as pd
df = pd.read_csv("Tasks_pandas\\Malayalam_actor_actress\\malayalam_actors_actresses.csv")
print(df.shape)
print(df.columns)
print(df.isnull().sum())
print(df.head())
print(df.tail())
print(df.info())