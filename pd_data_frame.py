
import pandas as pd

students ={
        "name":["Abin","Shajeer","Lijo","Shafi"],
        "age":[28,24,22,25],
        "qualification":["B-Tech","BCA","BA","BSC"]
}

df = pd.DataFrame(students)
print(df)

print(df[2:3])

print(df["age"])
print(df[["name","qualification"]])