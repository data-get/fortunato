#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from os.path import dirname, join

from setuptools import setup

setup(
    name='fortunato-ops',
    version='0.0.1',
    description='Happy, Lucky, Rich, Blessed Infrastructure',
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    author='Andrew Crouse',
    author_email='amcrouse@data-get.org',
    url='https://github.com/edmontonpy/fortunato',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # See: http://pypi.python.org/pypi?%3Aaction=list_classifiers
    ],
    keywords=[
    ],
    scripts=[
    ],
    install_requires=[
        'ansible>=2.7.0',
    ],
)
