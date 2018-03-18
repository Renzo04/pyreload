# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from ..internal.DeadHoster import DeadHoster


class IfileIt(DeadHoster):
    __name__ = "IfileIt"
    __type__ = "hoster"
    __version__ = "0.34"
    __status__ = "stable"

    __pattern__ = r'^unmatchable$'
    __config__ = []  # @TODO: Remove in 0.4.10

    __description__ = """Ifile.it hoster plugin"""
    __license__ = "GPLv3"
    __authors__ = [("zoidberg", "zoidberg@mujmail.cz")]
