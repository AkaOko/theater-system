from PIL import Image, ImageDraw
import os

# Создаем директорию для favicon, если она не существует
favicon_dir = os.path.join('mama', 'theater_system', 'theater', 'static', 'theater', 'images')
os.makedirs(favicon_dir, exist_ok=True)

# Создаем новое изображение 32x32 пикселя
img = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Рисуем простой театральный символ (маска)
draw.ellipse([8, 8, 24, 24], fill='#2c3e50')
draw.ellipse([12, 12, 20, 20], fill='white')

# Сохраняем как ICO
favicon_path = os.path.join(favicon_dir, 'favicon.ico')
img.save(favicon_path, format='ICO')
print(f"Favicon создан: {favicon_path}") 