try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

install_requires = [
    'Django',
    'decorator>=3.3.2',
]

tests_require = [
    'django-jenkins>=0.11.0',
    'pep8>=0.6.1',
]

long_description = open('README.rst').read()

setup(
    name='django-ajaxutils',
    version="0.1.2",
    description='Ajax requests for Ponies',
    url='http://github.com/ahref/django-ajaxutils',
    packages=['ajaxutils'],
    zip_safe=True,
    license='BSD',
    classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
    long_description=long_description,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'test': tests_require},
    test_suite='runtests.runtests',
)
