#!/usr/bin/env python3
"""
Custom logging library.
"""

__title__ = 'PyLogging'
__version__ = '0.1.0.dev0'
__author__ = 'Hassan Pouralijan'
__license__ = 'MIT'
__copyright__ = 'Copyright 2020 by pouralijan'

from .py_logging import PyLogging


def get_version(number: bool = False) -> str:
    """
    return module version.
    """
    if number:
        return '.'.join(__version__.split('.')[:-1])
    return __version__
