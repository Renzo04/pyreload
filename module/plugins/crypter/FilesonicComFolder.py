# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from ..internal.DeadCrypter import DeadCrypter


class FilesonicComFolder(DeadCrypter):
    __name__ = "FilesonicComFolder"
    __type__ = "crypter"
    __version__ = "0.18"
    __status__ = "stable"

    __pattern__ = r'http://(?:www\.)?filesonic\.com/folder/\w+'
    __config__ = [("activated", "bool", "Activated", True)]

    __description__ = """Filesonic.com folder decrypter plugin"""
    __license__ = "GPLv3"
    __authors__ = [("zoidberg", "zoidberg@mujmail.cz")]
