import os
import sys
import django
from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application

# Добавляем путь к проекту в sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theater_system.settings')
django.setup()

# Получаем WSGI приложение
application = get_wsgi_application()

# Функция для обработки запросов
def handler(request):
    # Преобразуем запрос Vercel в запрос Django
    environ = {
        'REQUEST_METHOD': request.method,
        'PATH_INFO': request.path,
        'QUERY_STRING': request.query_string,
        'CONTENT_TYPE': request.headers.get('content-type', ''),
        'CONTENT_LENGTH': request.headers.get('content-length', ''),
        'HTTP_HOST': request.headers.get('host', ''),
        'wsgi.input': request.body,
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': False,
    }
    
    # Добавляем заголовки
    for key, value in request.headers.items():
        environ[f'HTTP_{key.upper().replace("-", "_")}'] = value
    
    # Обрабатываем запрос
    response = application(environ, lambda status, headers: None)
    
    # Возвращаем ответ
    return {
        'statusCode': response.status_code,
        'headers': dict(response.headers),
        'body': response.content.decode('utf-8'),
    } 