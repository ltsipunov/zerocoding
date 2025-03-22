import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(0,1,1000)
plt.title('Гистограмма нормальной случайной величины')
plt.hist(x, bins = 20)
plt.xlabel("Корзины с шагом 1")
plt.ylabel("Попало в корзину ")
plt.show()

print(x[:10] )

