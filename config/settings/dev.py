from .base import *

DEBUG = True

CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ['*']
REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)
