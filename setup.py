#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="chartio_embed",
    version="0.1.0",
    author="Stephen",
    author_email="lewchuk@inkling.com",
    packages=[
        "chartio_embed",
    ],
    include_package_data=True,
    install_requires=[
        "Django==1.7.6",
    ],
    zip_safe=False,
    scripts=["chartio_embed/manage.py"],
)
