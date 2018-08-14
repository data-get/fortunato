#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from os.path import dirname, join

from setuptools import find_packages, setup


tests_require = [
    'coverage>=4.5.1, < 5.0',
    'flake8>=3.5.0, < 4.0',
    'pycodestyle==2.3.1',
    'tblib>=1.3.2, < 2.0',
    'pyflakes>=1.6.0, < 2.0'
]

setup(
    name='fortunato',
    version='0.0.1',
    description='Happy, Lucky, Rich, Blessed',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    author='Andrew Crouse',
    author_email='amcrouse@data-get.org',
    url='https://github.com/edmontonpy/fortunato',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # See: http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords=[
        'fortunato'
    ],
    scripts=[
        'bin/fortunato',
        'manage.py',
    ],
    install_requires=[
        'django>=2.1.0',
    ],
    test_suite="fortunato",
    tests_require=tests_require,
    extras_require={
        'dev': tests_require,
    },
)
