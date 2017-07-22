#!/usr/bin/env python3
"""
logger.py
keylogger

Defines Logger class for easy logging.

Created by Jakob Beckmann on 21/07/2017.
"""

import time
import os

class Logger:
    """
    Logger class to easily write timestamped messages to a file.
    """
    def __init__(self, filename="key.log"):
        """
        Initialise with filename. Creates direcotry ~/Library/Logs/keylog2 if it does not exist.
        """
        self._logfile_path = os.path.expanduser("~/Library/Logs/keylog2")
        self._filename = os.path.join(self._logfile_path, filename)

        # Create directory if not existing
        if not os.path.exists(self._logfile_path):
            os.makedirs(self._logfile_path)

        # Create a new line to show logger launched
        self.write("----------", prefix="---------- ")


    def write(self, text, prefix="", curr_time=None, end="\n"):
        """
        Writes to logfile with prefix timestamp text end. The timestamp can be set with optional parameter curr_time.
        """
        if curr_time is None:
            curr_time = time.localtime()
        timestamp = time.strftime("[%d/%m/%y - %H:%M:%S] ", curr_time)
        with open(self._filename, 'a') as fh:
            fh.write(prefix + timestamp + text + end)



