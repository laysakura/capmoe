#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


tests_require = [
    'nose',
    'coverage',
    'nose-cov',
    'nose-parameterized',
    'rainbow_logging_handler',
],

setup(
    name             = 'capmoe',
    description      = 'CapMoe - Cap Beer cap image search, CV algorithms and their API',
    long_description = open('README.rst').read(),
    url              = 'https://github.com/laysakura/capmoe',
    license          = 'LICENSE.txt',
    version          = '0.0.3',
    author           = 'Sho Nakatani',
    author_email     = 'lay.sakura@gmail.com',
    tests_require    = tests_require,
    install_requires = [
        'numpy',
        'redis',
        'simplejson',
        # following packages are necessary but not installed from PyPI
        # 'cv2',
        # 'pyflann',
    ],
    extras_require = {
        'testing': tests_require,
    },
    packages = [
        'capmoe',
        'capmoe.api',
        'capmoe.cv',
        'capmoe.util',
    ],
    scripts = [
    ],
    classifiers = '''
Programming Language :: Python
Development Status :: 4 - Beta
Programming Language :: Python :: 2.7
Operating System :: POSIX :: Linux
'''.strip().splitlines()
)
