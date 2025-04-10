from PIL import Image, ImageDraw

# Создаем новое изображение 32x32 пикселя
img = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Рисуем простой театральный символ (маска)
draw.ellipse([8, 8, 24, 24], fill='#2c3e50')
draw.ellipse([12, 12, 20, 20], fill='white')

# Сохраняем как ICO
img.save('theater/static/theater/images/favicon.ico', format='ICO') 