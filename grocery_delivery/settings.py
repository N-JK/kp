"""
Django settings for grocery_delivery project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!#xe&f@#vd%g$!^8a12d!2yq+v((a11rdy*tr5%3c2g***@+*^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'store.apps.StoreConfig',
    'crispy_forms',
    'crispy_bootstrap4',
    'django.contrib.sites',
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

ROOT_URLCONF = 'grocery_delivery.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'store.context_processors.admin_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'grocery_delivery.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Authentication settings
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'achuss1235@gmail.com'  # Replace this with your actual Gmail address
EMAIL_HOST_PASSWORD = 'tpod pjtv wcuj wxwu'  # Replace this with your actual 16-character App Password
DEFAULT_FROM_EMAIL = 'achuss1235@gmail.com'  # Replace with your actual Gmail address

# To get your Gmail App Password:
# 1. Go to your Google Account settings (https://myaccount.google.com/security)
# 2. Enable 2-Step Verification if not already enabled
# 3. Go to App Passwords (under 'Signing in to Google')
# 4. Select 'Mail' and 'Other (Custom name)'
# 5. Enter 'Django Fresh Mart' as the name
# 6. Click Generate
# 7. Copy the 16-character password (it looks like: abcd efgh ijkl mnop)
# 8. Paste it above in EMAIL_HOST_PASSWORD

# Stripe settings
STRIPE_PUBLISHABLE_KEY = 'pk_test_51QzECNC4houORSwmGg6CVvI5sth1UCXy7QxH2MILEheKu2yv4EmAJr8wSHpFCiDPgG3ezL33FxSuK1Ai8x9mtSFI00nf68TvUr'
STRIPE_SECRET_KEY = 'sk_test_51QzECNC4houORSwmWfOJRkJ2iMvX1rw2CgnhF71fJsE72TapPvQ3ijnwefr8OaSxNhsCPoOUGGJBnJKTyDskzpYf00GXwMtBzk'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1

# Password Reset Settings
PASSWORD_RESET_TIMEOUT = 14400  # 4 hours