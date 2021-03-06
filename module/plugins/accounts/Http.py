# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from ..internal.Account import Account


class Http(Account):
    __name__ = "Http"
    __type__ = "account"
    __version__ = "0.07"
    __status__ = "testing"

    __description__ = """Http dummy account plugin"""
    __license__ = "GPLv3"
    __authors__ = [("zoidberg", "zoidberg@mujmail.cz")]

    info_threshold = 1000000
    login_timeout = 1000000
