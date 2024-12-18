INSTALLED_APPS = [
    ...
    'school',
]

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'school/static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'