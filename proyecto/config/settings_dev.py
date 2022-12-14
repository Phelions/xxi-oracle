"""local runserver settings"""

import os

from .settings import BASE_DIR

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "nzcm$_84@4qd6e^#yinut58p%r0+qlveqjcg8@7rvq@-t)zxv1"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'sigloxxi_high',
        'USER': 'ADMIN',
        'PASSWORD': 'H4MC4HABixRz',
    }
}
# Static Files

STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR ,'src/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'proyecto/src/static')