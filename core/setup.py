#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import site
import sys
from setuptools import setup

# workaround https://github.com/pypa/pip/issues/7953
site.ENABLE_USER_SITE = "--user" in sys.argv[1:]
# Workaround for https://github.com/pypa/setuptools/issues/2938
#   Does not work: python3 -m pip install --user --editable
#   Use: python3 setup.py develop --user

setup()
