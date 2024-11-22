import os
from pathlib import Path

# Путь к корню проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Безопасность ключа
SECRET_KEY = 'your-secret-key'

# Режим отладки
DEBUG = True

# Разрешенные хосты
ALLOWED_HOSTS = []

# Приложения Django
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'events',  # Ваше приложение
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Корневой URLconf
ROOT_URLCONF = 'event_platform.urls'

# Шаблоны
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Укажите директорию для шаблонов
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# База данных
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',  # База данных SQLite (для разработки)
    }
}

# Язык и часовой пояс
LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'

# Форматы данных
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Статические файлы (CSS, JavaScript, изображения)
STATIC_URL = '/static/'

# Путь к директории для статических файлов
STATICFILES_DIRS = [BASE_DIR / 'static']

# Укажите путь для медиа-файлов (для изображений, видео и других медиа)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Автоматическая загрузка файлов статики
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = 'event_list'  # Перенаправление после успешного входа
LOGOUT_REDIRECT_URL = 'event_list'  # Перенаправление после выхода


# Для безопасности и других настройок можно добавить параметры:
# SECURE_SSL_REDIRECT = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True

