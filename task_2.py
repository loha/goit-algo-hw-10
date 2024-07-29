import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0
b = 2

# Кількість випадкових точок для методу Монте-Карло
N = 10000

# Генерація випадкових точок
x_random = np.random.uniform(a, b, N)
y_random = np.random.uniform(0, f(b), N)

# Обчислення кількості точок під кривою
under_curve = y_random < f(x_random)

# Обчислення площі під кривою
area_mc = (b - a) * f(b) * np.sum(under_curve) / N

# Аналітичний результат для порівняння
area_analytical, _ = quad(f, a, b)

# Виведення результатів
print(f"Метод Монте-Карло: {area_mc:.4f}")
print(f"Аналітичний результат: {area_analytical:.4f}")

# Побудова графіка
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

fig, ax = plt.subplots()
ax.plot(x, y, 'r', linewidth=2)
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title(f'Графік інтегрування f(x) = x^2 від {a} до {b}')
plt.grid()
plt.show()
