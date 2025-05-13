import vispy
vispy.use('pyqt5')
import numpy as np
from vispy import app, scene
from vispy.visuals import markers

# Генерация 10 миллионов случайных точек
N = 10_000_000
positions = np.random.uniform(-100, 100, (N, 3)).astype(np.float32)
sizes = np.random.uniform(2, 5, N).astype(np.float32)
colors = np.random.uniform(0.0, 1.0, (N, 4)).astype(np.float32)
colors[:, 3] = 0.5  # прозрачность

# Создание сцены
canvas = scene.SceneCanvas(keys='interactive', show=True, bgcolor='black')
view = canvas.central_widget.add_view()
view.camera = scene.cameras.TurntableCamera(fov=45, distance=300)

# Добавление точек как маркеров (шариков)
scatter = markers()
scatter.set_data(positions, face_color=colors, size=sizes)
view.add(scatter)

# Анимация (движение точек)
def update(event):
    global positions
    # Здесь твоя функция движения, пока — случайный сдвиг
    positions += (np.random.rand(*positions.shape) - 0.5) * 0.2
    scatter.set_data(positions, face_color=colors, size=sizes)

# Обновление каждые 10 мс
timer = app.Timer(interval=0.01, connect=update, start=True)

# Запуск
app.run()
