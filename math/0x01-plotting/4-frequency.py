#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

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
