import matplotlib.pyplot as plt
import numpy as np


x = np.random.rand(10)
y = np.random.rand(10)
plt.Figure(figsize=(10,5))
plt.title('Диаграмма рассеяния независимых равномерно распределенных величин ')
plt.scatter(x,y)
plt.xlabel("ось Х")
plt.ylabel("ось Y")
plt.show()
print(x[:5],y[:5]  )

