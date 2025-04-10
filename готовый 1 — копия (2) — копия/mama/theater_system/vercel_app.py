import os
import sys
import django

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theater_system.settings')
django.setup()

# Инициализация базы данных
from django.db import connection
with connection.cursor() as cursor:
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='auth_user'")
    if not cursor.fetchone():
        # Если таблица auth_user не существует, выполняем миграции
        from django.core.management import call_command
        call_command('migrate')
        
        # Создаем суперпользователя
        from django.contrib.auth.models import User
        if not User.objects.filter(username='superadmin').exists():
            User.objects.create_superuser(
                username='superadmin',
                email='superadmin@example.com',
                password='admin123'
            )
            print("Суперпользователь успешно создан!")

# Получаем WSGI приложение
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Vercel requires the app variable to be named 'app'
app = application 