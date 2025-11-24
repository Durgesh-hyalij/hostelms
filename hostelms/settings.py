import os
from pathlib import Path
import dj_database_url

# --------------------
# BASE DIR
# --------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# --------------------
# SECRET KEY
# --------------------
# IMPORTANT: Replace this with your actual secret key (from Railway vars)
SECRET_KEY = os.environ.get("SECRET_KEYdjango-insecure-t7v7n6dhd6l87a)r(i6eo!-z(xag8qd_cn3%f(0dle6vs^3n=(", "dev-secret-key")

# --------------------
# DEBUG
# --------------------
# Railway → DEBUG=False in environment variables
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# --------------------
# ALLOWED HOSTS
# --------------------
ALLOWED_HOSTS = [
    "*",   # or directly: "durgeshhostel.up.railway.app"
]

# --------------------
# CSRF TRUSTED ORIGINS
# --------------------
CSRF_TRUSTED_ORIGINS = [
    "https://*.up.railway.app",
    "https://durgeshhostel.up.railway.app",
]

# --------------------
# APPLICATIONS
# --------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Our Apps
    'accounts',
    'attendance',
    'fees',
    'discipline',
    'hostel',
    'notices',
]

# --------------------
# MIDDLEWARE
# --------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # WhiteNoise for static files
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# --------------------
# URLS
# --------------------
ROOT_URLCONF = 'hostelms.urls'

# --------------------
# TEMPLATES
# --------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

# --------------------
# WSGI
# --------------------
WSGI_APPLICATION = 'hostelms.wsgi.application'

# --------------------
# DATABASE (PostgreSQL for Railway)
# --------------------
DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR}/db.sqlite3",
        conn_max_age=600,
        ssl_require=False
    )
}

# --------------------
# PASSWORD VALIDATION
# --------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]

# --------------------
# INTERNATIONALIZATION
# --------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

# --------------------
# STATIC FILES (Railway)
# --------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),  # if you have a static folder
]

# --------------------
# SECURITY (Important for Production)
# --------------------
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = False  # Railway already handles HTTPS

# --------------------
# DEFAULT PRIMARY KEY
# --------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
