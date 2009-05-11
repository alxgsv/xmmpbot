#!/usr/bin/env python

import sys
sys.path = ['.']+sys.path
import xmppbot

from distutils.core import setup

PACKAGE = 'xmppbot'
VERSION = xmppbot.__version__

setup(name=PACKAGE,
      version=VERSION,
      description='An xmpp bot',
      author='Thomas Perl and Alex Gusev',
      license='GPLv3 or later',
      py_modules=['xmppbot', 'presence_storage', 'message_parsers'],
      packages = ['message_parsers'],
      requires=['xmpppy'],
)

