DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        },
    }
INSTALLED_APPS=[
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sessions',
    'django.contrib.sites',

    # Included to fix Disqus' test Django which solves IntegrityMessage case
    'django.contrib.contenttypes',

    'ajaxutils_tests',
    ]
ROOT_URLCONF='ajaxutils_tests.urls'
DEBUG=False
TEMPLATE_DEBUG=True
JENKINS_TASKS=(
    #            'django_jenkins.tasks.run_pylint',
    #            'django_jenkins.tasks.run_pep8',
    #            'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.django_tests',
    )
SITE_ID=1
