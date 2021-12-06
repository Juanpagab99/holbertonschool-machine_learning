#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

rows = ('apples', 'bananas', 'oranges', 'peaches')
columns = ('Farrah', 'Fred', 'Felicia')
index = columns
colors = ('r', 'y', '#ff8000', '#ffe5b4')
bars_width = 0.5
num_rows = len(fruit)
offset = np.zeros(len(columns))


for row in range(num_rows):
    plt.bar(index, fruit[row], bars_width, bottom=offset,
            color=colors[row], label=rows[row])
    offset = offset + fruit[row]


plt.legend()
plt.yticks(np.arange(0, 90, 10))
plt.ylabel('Quantity of Fruit')
plt.title("Number of Fruit per Person")

plt.show()
