import os
import sys
import django

# Добавляем путь к проекту в sys.path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(project_root, 'mama', 'theater_system'))

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mama.theater_system.theater_system.settings')
django.setup()

# Получаем WSGI приложение
from django.core.wsgi import get_wsgi_application
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
        'wsgi.url_scheme': 'https',
        'SERVER_NAME': request.headers.get('host', '').split(':')[0],
        'SERVER_PORT': '443',
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