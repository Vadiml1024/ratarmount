#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from setuptools import setup

scriptPath = os.path.abspath( os.path.dirname( __file__ ) )
with open( os.path.join( scriptPath, 'README.md' ), encoding = 'utf-8' ) as file:
    readmeContents = file.read()

with open( 'requirements.txt', 'rt' ) as file:
    requirements = file.read().splitlines()

setup(
    name             = 'ratarmount',
    version          = '0.9.0',

    description      = 'Random Access Read-Only Tar Mount',
    url              = 'https://github.com/mxmlnkn/ratarmount',
    author           = 'Maximilian Knespel',
    author_email     = 'mxmlnkn@github.de',
    license          = 'MIT',
    classifiers      = [ 'License :: OSI Approved :: MIT License',
                         'Development Status :: 4 - Beta',
                         'Natural Language :: English',
                         'Operating System :: MacOS',
                         'Operating System :: POSIX',
                         'Operating System :: Unix',
                         'Operating System :: Microsoft :: Windows',
                         'Programming Language :: Python :: 3',
                         'Programming Language :: Python :: 3.6',
                         'Programming Language :: Python :: 3.7',
                         'Programming Language :: Python :: 3.8',
                         'Programming Language :: Python :: 3.9',
                         'Topic :: System :: Archiving' ],

    long_description = readmeContents,
    long_description_content_type = 'text/markdown',

    py_modules       = [ 'ratarmount' ],
    install_requires = [ 'fusepy',
                         'indexed_bzip2>=1.1.2; platform_system=="Linux"',
                         'indexed_bzip2>=1.3.0; platform_system!="Linux"',
                         'indexed_gzip>=1.5.3',
                         'indexed_zstd>=1.3.1; sys_platform=="darwin"',
                         'indexed_zstd>=1.2.2; platform_system!="Windows"',
                         'dataclasses; python_version < "3.7.0"' ],
    # Make these optional requirements because they have no binaries on PyPI meaning they are built from source
    # and will fail if system dependencies are not installed.
    extras_require   = {
                            'full' : [ 'cffi; platform_system!="Windows"',
                                       'lzmaffi; platform_system!="Windows"' ],
                            # cffi dependency seems to be configured wrong in lzmaffi,
                            # therefore also list it here before lzmaffi:
                            # https://github.com/r3m0t/backports.lzma/issues/3
                            'xz' : [ 'cffi; platform_system!="Windows"',
                                     'lzmaffi; platform_system!="Windows"' ],
                       },
    entry_points = { 'console_scripts': [ 'ratarmount=ratarmount:cli' ] }
)
