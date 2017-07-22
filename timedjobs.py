#!/usr/bin/env python3
"""
timedjobs.py
keylogger

Creates a timer class to perform timed jobs.

Created by Jakob Beckmann on 21/07/2017.
"""

import time
import threading

class Job(threading.Thread):
    """
    Job subclass of Thread running a target function while logging.
    """
    INFINITE = -1

    def __init__(self, thread_id, name, logger,
                 function, args=(), repeat=INFINITE):
        """
        Initialises the object. name is used by the logger to give constructive information about running threads.
        """
        super().__init__()
        self._thread_id =  thread_id
        self._name = name
        self._logger = logger
        self._function = function
        self._args = args
        self._count = repeat
        self._timer = 0

    def set_timer(self, timer):
        """
        Set timer if target function should only run every so often.
        """
        self._timer = timer

    def run(self):
        """
        Override of the Thread function that is called when thread is launched.
        """
        self._logger.write("Thread \"" + self._name + "\" started ... ",
                           prefix="[+]")

        while self._count > 0 or self._count == self.INFINITE:
            self._function(self._args)
            if self._count != self.INFINITE:
                self._count -= 1
            if self._timer != 0:
                time.sleep(self._timer)

        self._logger.write("Thread \"" + self._name + "\" finished.",
                           prefix="[+]")
