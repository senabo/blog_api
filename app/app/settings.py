import os
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# ENV setting
env = environ.Env()

# reading .env file
environ.Env.read_env()

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = env.str("SECRET_KEY")
SECRET_KEY = "ys(a4zs+hl$rwgvji9cm0h#qf*$@0lu!3-*t#df$(r4mj&u==)"

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = env.bool("DEBUG", default=False)
DEBUG = False

# ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1', 'developstoday.herokuapp.com']

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "rest_framework",
    "rest_framework.authtoken",
    "djoser",
    "django_crontab",
    "blog.apps.BlogConfig",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        # "NAME": env("POSTGRES_DB"),
        # "NAME": env("DB_NAME"),
        # "USER": env("DB_USER"),
        # "PASSWORD": env("DB_PASSWORD"),

        "NAME": os.environ.get('DB_NAME'),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        # "HOST": "db",
        "HOST": os.environ.get("DB_HOST"),
        "PORT": "5432",
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = "/static/"

# DJOSER settings
DJOSER = {
    "PASSWORD_RESET_CONFIRM_URL": "#/password/reset/confirm/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "#/username/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "#/activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": False,
    "SERIALIZERS": {},
}

# REST_FRAMEWORK settings
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 30,
}


# CRONTAB settings
CRONJOBS = [("* * * * *", "blog.cron.reset_post_upvotes")]

