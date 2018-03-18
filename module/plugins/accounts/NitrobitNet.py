# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import re
import time

import pycurl

from ..internal.Account import Account


class NitrobitNet(Account):
    __name__ = "NitrobitNet"
    __type__ = "account"
    __version__ = "0.01"
    __status__ = "testing"

    __description__ = """Nitrobit.net account plugin"""
    __license__ = "GPLv3"
    __authors__ = [("GammaC0de", "nitzo2001[AT]yahoo[DOT]com")]

    def grab_info(self, user, password, data):
        return {'premium': True,
                'validuntil': None,
                'trafficleft': None}

    def signin(self, user, password, data):
        #: no way to sign in until we actually download something
        self.skip_login()
