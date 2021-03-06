import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


SECRET_KEY = '!ie+&jchd8c*ul14xpx@#swt66x0e0)+@*dwj1y5ol(fjv2+uy'


DEBUG = True # not os.environ.get('DEBUG', False)
PROD = not DEBUG

ALLOWED_HOSTS = ['*']




INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'magapp',
    'accounts',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'rest_auth.registration',
    
    'corsheaders',

    'drf_yasg',

    'channels',

    
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ]
}

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

SWAGGER_SETTINGS = {
    'VALIDATOR_URL': 'http://localhost:8189',
    'USE_SESSION_AUTH': False,
}


CORS_ORIGIN_ALLOW_ALL = True

AUTH_USER_MODEL = 'accounts.CustomUser'

ROOT_URLCONF = 'magproject.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'magproject.wsgi.application'
ASGI_APPLICATION = "magproject.routing.application"

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

############################################################################
if PROD:
    DATABASES = {                                                          #
        'default': {                                                       #
            'ENGINE': 'django.db.backends.postgresql_psycopg2',            #
            'NAME': 'mag',                                                 #
            'USER': 'mag_user',                                            #
            'PASSWORD': '12345',                                           #
            'HOST': '127.0.0.1',                                            #
            'PORT': 5432, 
            'TEST': {
                'NAME': 'mag'
                    }                                                 
        }                                                                  #
    }              
else:
    DATABASES = {                                                          #
        'default': {                                                       #
            'ENGINE': 'django.db.backends.postgresql_psycopg2',            #
            'NAME': 'mag',                                                 #
            'USER': 'mag_user',                                            #
            'PASSWORD': '12345',                                           #
            'HOST': '127.0.0.1',                                           #
            'PORT': 5432,                                                  #
        }                                                                  #
    }                                                                      #
############################################################################


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'


if PROD:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
else:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'tech.academy.user2@gmail.com'
EMAIL_HOST_PASSWORD = 'fsqcyadagqipthcz'
EMAIL_PORT = 587
EMAIL_USE_TLS = True