import os
import django
from django.contrib.auth.models import User
from django.db import connection

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theater_system.settings')
django.setup()

# Инициализация базы данных
with connection.cursor() as cursor:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='auth_user'")
    if not cursor.fetchone():
        # Если таблица auth_user не существует, выполняем миграции
        from django.core.management import call_command
        call_command('migrate')
        
        # Создаем суперпользователя
        if not User.objects.filter(username='superadmin').exists():
            User.objects.create_superuser(
                username='superadmin',
                email='superadmin@example.com',
                password='admin123'
            )
            print("Суперпользователь успешно создан!")

# Импорт WSGI приложения
from theater_system.wsgi import application

# Vercel requires the app variable to be named 'app'
app = application 