#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# Especificar los tamaños
fig = plt.figure(figsize=(6, 6))
fig.suptitle("All in one")
grid = plt.GridSpec(3, 2, wspace=1.5, hspace=1.5)

# Primer gráfica
ax1 = fig.add_subplot(grid[0, 0])
plt.xlim(0, 10)
plt.plot(y0, "r")

# Segunda gráfica
ax2 = fig.add_subplot(grid[0, 1])
plt.xlabel('Height (in)')
plt.ylabel('Weight (lbs)')
plt.title("Men's Height vs Weight")
plt.scatter(x1, y1, c="magenta")

# Tercera gráfica
ax3 = fig.add_subplot(grid[1, 0])
plt.title("Exponential Decay of C-14")
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")
plt.yscale('log')
plt.xlim(0, 28650)
plt.plot(x2, y2)

# Cuarta gráfica
ax4 = fig.add_subplot(grid[1, 1])
plt.title("Exponential Decay of Radioactive Elements")
plt.xlabel("Time (years)")
plt.ylabel("Fraction Remaining")
plt.xlim(0, 20000)
plt.ylim(0, 1)
plt.plot(x3, y31, 'r', linestyle="dashed", label="C-14")
plt.plot(x3, y32, 'g', label="Ra-226")
plt.legend()

# Quinta figura
ax5 = fig.add_subplot(grid[2, :2])
plt.xlim(0, 100)
plt.ylim(0, 30)
limite = np.arange(0, 110, 10)
limites = np.arange(0, 35, 5)
plt.xticks(limite)
plt.yticks(limites)
plt.title("Project A")
plt.xlabel("Grades")
plt.ylabel("Number of Students")
plt.hist(student_grades, bins=limite, edgecolor='black', linewidth=1.2)

plt.show()
