#!/usr/bin/env python
from setuptools import setup

setup(
    name="autodebug",
    version="1.0.1",
    author="Michał Podeszwa",
    author_email="michal.podeszwa@gmail.com",
    description=("Importing this module enables automatic post mortem debugging"
                 " upon any exception. It uses module specified in envvar"),
    license="BSD",
    keywords="debugger debug automatic auto auto-debug",
    url = "https://github.com/MichalPodeszwa/autodebug",
    packages=["autodebug"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Software Development :: Debuggers"
    ]
)
