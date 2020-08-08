#!/usr/bin/env python3
"""
Custom logging library.
"""

import logging
import logging.handlers


class PyLogging(logging.Logger):
    """
    PyLogging class.
    """
    def __init__(self, name: str = None, level: int = logging.NOTSET) -> None:
        """
        PyLogging init function.

        Args:
            name: Logger name.
            level: Logger level.
        """
        super().__init__(name, level)

        self.formatter = logging.Formatter('%(filename)s: %(message)s')
        if name:
            self.formatter = logging.Formatter('%(name)s: %(message)s')

        self.setLevel(level)

        consol_handler = logging.StreamHandler()
        consol_handler.setFormatter(self.formatter)
        self.addHandler(consol_handler)
