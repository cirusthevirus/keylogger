#!/usr/bin/env python3

""" Use: python3 setup.py py2app -A """

from setuptools import setup
import py2app

APP = ["keylog.py"]
DATA_FILES = []
OPTIONS = {
    'iconfile': 'klog.icns',
    'plist': 'Info.plist'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)
