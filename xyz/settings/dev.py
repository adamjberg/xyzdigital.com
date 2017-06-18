from xyz.settings.base import *

DEBUG = True
INSTALLED_APPS += (
    'debug_toolbar',  # and other apps for local development
)

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES += (
    "debug_toolbar.middleware.DebugToolbarMiddleware",
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
