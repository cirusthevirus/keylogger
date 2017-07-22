# keylogger
## Disclaimer
This keylogger is written as a proof of concept and SHOULD NOT be used for illegal purposes. I wrote this as an educative exercise to learn some PyObjC and low-level OS access on OS X.

## Description
Keylogger running in the background to log keystrokes and mouse button clicks. It makes use of the PyObjC bridge. Of course, this makes the footprint of the keylogger much bigger than if written in plain objective-c. However, I dislike objective-c.

## "Compiling"
Simply run `python3 setup.py py2app -A` in the terminal while in the directory with all files.


## Issues
For some reason, the CGEventTap does not tap regular keyboard button presses. It only taps special key presses and releases (from kCGEventFlagsChanged) and left mouse button clicks (from kCGEventLeftMouseDown).

Note that this problem persists when the keylogger is written in objective-c (I have done it and the results are the same).

## Future Improvements
- Keylogger takes low resolution screenshots each time the mouse button is pressed.
- Keylogger sends emails of the log files to a hardcoded email address.
- Keylogger encrypts before logging keystrokes to log files.
- Keylogger copies itself to run as a deamon on host machine.
