import os
import json

#########################
#                       #
#   Required settings   #
#                       #
#########################

ALLOWED_HOSTS = os.environ.get(
    "ALLOWED_HOSTS",
    "localhost"
).split(",")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ["DB_NAME"],
        'USER': os.environ["DB_USER"],
        'PASSWORD': os.environ["DB_PASSWORD"],
        'HOST': os.environ["DB_HOST"],
        'PORT': os.environ["DB_PORT"],
        'CONN_MAX_AGE': 300,
    }
}

REDIS = {

    'tasks': {

        'HOST': os.environ["REDIS_HOST"],
        'PORT': int(os.environ["REDIS_PORT"]),

        'USERNAME': '',

        'PASSWORD': os.environ.get(
            "REDIS_PASSWORD",
            ""
        ),

        'DATABASE': 0,

        'SSL': False,

    },

    'caching': {

        'HOST': os.environ["REDIS_CACHE_HOST"],

        'PORT': int(
            os.environ["REDIS_CACHE_PORT"]
        ),

        'USERNAME': '',

        'PASSWORD': os.environ.get(
            "REDIS_CACHE_PASSWORD",
            ""
        ),

        'DATABASE': 1,

        'SSL': False,

    }

}

SECRET_KEY = os.environ["SECRET_KEY"]

API_TOKEN_PEPPERS = {
    1: "i=rB1b0#E0s2$i6)iFeB)h#(QWIF_8dHr8A7F!OXJ=lxFf&wb4"
}

#########################
#                       #
#   Optional settings   #
#                       #
#########################

DEBUG = False

TIME_ZONE = os.environ.get(
    "TIME_ZONE",
    "Asia/Manila"
)

DEFAULT_LANGUAGE = 'en-us'

ADMINS = []

AUTH_PASSWORD_VALIDATORS = []

BASE_PATH = ''

CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = []

CORS_ORIGIN_REGEX_WHITELIST = []

CSRF_COOKIE_NAME = 'csrftoken'

CSRF_TRUSTED_ORIGINS = [
    "http://netbox.local",
    "http://localhost:8000",
]

EMAIL = {

    'SERVER': 'localhost',

    'PORT': 25,

    'USERNAME': '',

    'PASSWORD': '',

    'USE_SSL': False,

    'USE_TLS': False,

    'TIMEOUT': 10,

    'FROM_EMAIL': '',

}

STREAMING_EXPORTS = False

EXEMPT_VIEW_PERMISSIONS = []

LOGGING = {}

LOGIN_PERSISTENCE = False

LOGIN_TIMEOUT = None

LOGIN_FORM_HIDDEN = False

LOGOUT_REDIRECT_URL = 'home'

METRICS_ENABLED = False

PLUGINS = [

    p.strip()

    for p in os.environ.get(
        "NETBOX_PLUGINS",
        ""
    ).split(",")

    if p.strip()

]

PLUGINS_CONFIG = {

    "netbox_topology_views": {

        "allow_coordinates_saving": True,

        "always_save_coordinates": True

    },

    "netbox_lifecycle": {

    }

}

REMOTE_AUTH_ENABLED = False

REMOTE_AUTH_BACKEND = 'netbox.authentication.RemoteUserBackend'

REMOTE_AUTH_HEADER = 'HTTP_REMOTE_USER'

REMOTE_AUTH_USER_FIRST_NAME = 'HTTP_REMOTE_USER_FIRST_NAME'

REMOTE_AUTH_USER_LAST_NAME = 'HTTP_REMOTE_USER_LAST_NAME'

REMOTE_AUTH_USER_EMAIL = 'HTTP_REMOTE_USER_EMAIL'

REMOTE_AUTH_AUTO_CREATE_USER = True

REMOTE_AUTH_DEFAULT_GROUPS = []

REMOTE_AUTH_DEFAULT_PERMISSIONS = {}

RELEASE_CHECK_URL = None

RQ_DEFAULT_TIMEOUT = 300

SESSION_COOKIE_NAME = 'sessionid'

SESSION_FILE_PATH = None
