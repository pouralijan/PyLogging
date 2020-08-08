#!/usr/bin/env python3
"""
PyLogging setup.py.
"""

try:
    from setuptools import setup
    from setuptools import find_packages
except ImportError as error:
    raise SystemExit(error)

from py_logging import get_version

setup(
    name="PyLogging",
    version=get_version(),
    description="A minimal python logging library",
    author="Hassan Pouralijan",
    author_email="pouralijan@gmail.com",
    packages=find_packages()
)
