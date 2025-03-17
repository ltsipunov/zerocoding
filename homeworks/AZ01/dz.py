import pandas as pd

df= pd.read_csv('datasets/dz.csv')
print(' ------ Фрагмент датафрейма dz ------------ ')
print(df.head(10) )
print(' ------ Состав данных dz ------------ ')
print(df.info())
print(' ------ Средние зарплаты по городам из dz ------------ ')
print( df.groupby('City',dropna=False).Salary.mean() )