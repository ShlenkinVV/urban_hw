"""
author - Shlenkin Vladimir
GitHub - ShlenkinVV


"""
import matplotlib.pyplot as plt
import numpy as np


def v(x):
    return -np.cos(x * x) * (1 + np.sin(5 * x) + 3 * np.exp(x))

def derivative(x):
    h = 1e-5  # Маленький шаг для численного дифференцирования
    return (v(x + h) - v(x - h)) / (2 * h)

# Генерация случайных данных
x = np.linspace(2, 9, 500)
y = v(x)
dy = derivative(x)

sign_changes = np.where(np.diff(np.sign(dy)))[0]

plt.plot(x, y, label='v(x)', color='blue')
plt.xlabel('x')
plt.ylabel('v(x)')

plt.grid(True)

plt.scatter(x[sign_changes], v(x[sign_changes]), color='red', zorder=5, label='Изменение знака производной')
plt.legend()

plt.show()