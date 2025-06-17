import main_2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

# Параметры
num_balls = 2000
space_size = 10000
max_radius = 0.00001
step_size = 10  # Максимальное перемещение за 1 шаг

# Инициализация позиций и радиусов
positions = np.random.uniform(-space_size, space_size, size=(num_balls, 3))
radii = np.random.uniform(0.1, max_radius, size=num_balls)

# Настройка графика
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

scat = ax.scatter(positions[:, 0], positions[:, 1], positions[:, 2], s=radii * 500)

ax.set_xlim(-space_size, space_size)
ax.set_ylim(-space_size, space_size)
ax.set_zlim(-space_size, space_size)

def update(frame):
    global positions
    # Случайное смещение
    movement = np.random.uniform(-step_size, step_size, size=(num_balls, 3))
    positions += movement

    # Обновление точек
    scat._offsets3d = (positions[:, 0], positions[:, 1], positions[:, 2])
    return scat,

# Анимация
ani = FuncAnimation(fig, update, frames=20, interval=10, blit=False)
plt.show()

