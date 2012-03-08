DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
    },
}

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.contenttypes',

    'ajaxutils_tests',
]

ROOT_URLCONF = 'ajaxutils_tests.urls'
DEBUG = False
TEMPLATE_DEBUG = True

SITE_ID=1
