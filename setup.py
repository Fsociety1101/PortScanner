#!/usr/bin/env python
#This is the setup file
#To run this type python setup.py
from distutils.core import setup
import subprocess

subprocess.call('pip3 install datetime pyfiglet termcolor colorama multiprocessing', shell=True)
