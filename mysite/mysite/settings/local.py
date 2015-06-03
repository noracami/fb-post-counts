from .base import *

SECRET_KEY = '&t0h$18+jv^3+uce9e4hzaakw$60jxb(f(r+@-*q6)mvq(fx&l'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}
