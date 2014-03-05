#!/usr/bin/env python

# Produce to release a new version:
#  - ./test_doc.py
#  - run tests (test_gdb.py and test_strace.py) with Python 2 and Python 3
#  - check version in ptrace/version.py
#  - set release date in the ChangeLog
#  - hg ci
#  - hg tag python-ptrace-x.y
#  - hg ci
#  - hg push
#  - ./setup.py sdist register bdist_wheel upload
#  - update the website home page (url, md5 and news)
#    https://bitbucket.org/haypo/python-ptrace/wiki/Home
#  - set version to n+1 (ptrace/version.py)
#  - hg ci
#  - hg push

from __future__ import with_statement

MODULES = ["ptrace", "ptrace.binding", "ptrace.syscall", "ptrace.debugger"]

SCRIPTS = ("strace.py", "gdb.py")

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'License :: OSI Approved :: GNU General Public License (GPL)',
    'Operating System :: OS Independent',
    'Natural Language :: English',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
]

with open('README') as fp:
    LONG_DESCRIPTION = fp.read()
with open('ChangeLog') as fp:
    LONG_DESCRIPTION += fp.read()

from imp import load_source
from os import path
from sys import argv
try:
    # setuptools supports bdist_wheel
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup

ptrace = load_source("version", path.join("ptrace", "version.py"))
PACKAGES = {}
for name in MODULES:
    PACKAGES[name] = name.replace(".", "/")

install_options = {
    "name": ptrace.PACKAGE,
    "version": ptrace.VERSION,
    "url": ptrace.WEBSITE,
    "download_url": ptrace.WEBSITE,
    "author": "Victor Stinner",
    "description": "python binding of ptrace",
    "long_description": LONG_DESCRIPTION,
    "classifiers": CLASSIFIERS,
    "license": ptrace.LICENSE,
    "packages": list(PACKAGES.keys()),
    "package_dir": PACKAGES,
    "scripts": SCRIPTS,
}

setup(**install_options)
