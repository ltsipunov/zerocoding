import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../PS05_scraping/divanpars/divanpars/spiders/divan.csv',encoding='cp1251')

plt.hist(df.price//1000,bins = 6)
plt.xlabel("Цена дивана тыс руб, с шагом 20 тыс ")
plt.ylabel("Диванов в диапазоне цены, шт")
plt.show()

f = open('divan.log','w')
f.write(  f"{df.head()}\n\n" )
f.write(  f"Распределение по цене {df.describe()}\n\n" )
f.write( f"------------- Срелняя цена дивана: {round( df.price.mean() )} руб.-----------------------------\n" )
f.close()