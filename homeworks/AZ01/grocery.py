import pandas as pd
df = pd.read_csv("datasets/Grocery_Inventory new v1.csv")

print('-------- HEAD 5 ----------')
print(df.head(5))
print('-------- DESCRIBE ----------')
print(df.describe())
print('-------- INFO ----------')
print(df.info())
