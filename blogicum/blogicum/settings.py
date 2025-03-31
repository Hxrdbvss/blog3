from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# STATIC settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static',]

# Прочие настройки
SECRET_KEY = 'django-insecure-3@l&wu*-kppk%-j3)1+@#q&ye@-rfn=8d@l%d^$a@%m)3)7*4s'
DEBUG = True
<<<<<<< HEAD
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
CSRF_FAILURE_VIEW = 'pages.views.csrf_failure_view'
=======
ALLOWED_HOSTS = []
>>>>>>> 9589b23700b83ab030eb2dcd4a8a573bcea6f430

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages',
    'blog',
<<<<<<< HEAD
    'django_bootstrap5'
=======
>>>>>>> 9589b23700b83ab030eb2dcd4a8a573bcea6f430
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'blogicum.urls'

<<<<<<< HEAD
TEMPLATES_DIR = BASE_DIR / 'templates'
=======
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
>>>>>>> 9589b23700b83ab030eb2dcd4a8a573bcea6f430

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
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

WSGI_APPLICATION = 'blogicum.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Настройки локализации
LANGUAGE_CODE = 'ru-RU'  # Русский язык
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Путь для хранения файлов переводов
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

<<<<<<< HEAD
# Медиафайлы
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'sent_emails'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# В конец файла settings.py
LOGIN_REDIRECT_URL = '/'  # После логина — на главную
LOGOUT_REDIRECT_URL = '/'  # После логаута — на главную
=======
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
>>>>>>> 9589b23700b83ab030eb2dcd4a8a573bcea6f430
