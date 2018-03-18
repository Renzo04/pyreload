# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from os.path import (
    exists,
    join,
)

import six


CONF_VERSION = 1


class ConfigParser:

    def __init__(self, configdir):
        """Constructor"""
        self.configdir = configdir
        self.config = {}

        if self.checkVersion():
            self.readConfig()

    def checkVersion(self):

        if not exists(join(self.configdir, "pyload.conf")):
            return False
        f = open(join(self.configdir, "pyload.conf"), "rb")
        v = f.readline()
        f.close()
        v = v[v.find(":")+1:].strip()

        if int(v) < CONF_VERSION:
            return False

        return True

    def readConfig(self):
        """reads the config file"""

        self.config = self.parseConfig(join(self.configdir, "pyload.conf"))

    def parseConfig(self, config):
        """parses a given configfile"""

        f = open(config)

        config = f.read()

        config = config.split("\n")[1:]

        conf = {}

        section, option, value, typ, desc = "","","","",""

        listmode = False

        for line in config:

            line = line.rpartition("#") # removes comments

            if line[1]:
                line = line[0]
            else:
                line = line[2]

            line = line.strip()

            try:

                if line == "":
                    continue
                elif line.endswith(":"):
                    section, none, desc = line[:-1].partition('-')
                    section = section.strip()
                    desc = desc.replace('"', "").strip()
                    conf[section] = { "desc" : desc }
                else:
                    if listmode:

                        if line.endswith("]"):
                            listmode = False
                            line = line.replace("]","")

                        value += [self.cast(typ, x.strip()) for x in line.split(",") if x]

                        if not listmode:
                            conf[section][option] = { "desc" : desc,
                                                      "type" : typ,
                                                      "value" : value}


                    else:
                        content, none, value = line.partition("=")

                        content, none, desc = content.partition(":")

                        desc = desc.replace('"', "").strip()

                        typ, option = content.split()

                        value = value.strip()

                        if value.startswith("["):
                            if value.endswith("]"):
                                listmode = False
                                value = value[:-1]
                            else:
                                listmode = True

                            value = [self.cast(typ, x.strip()) for x in value[1:].split(",") if x]
                        else:
                            value = self.cast(typ, value)

                        if not listmode:
                            conf[section][option] = { "desc" : desc,
                                                      "type" : typ,
                                                      "value" : value}

            except:
                pass

        f.close()
        return conf

    def cast(self, typ, value):
        """cast value to given format"""
        if not isinstance(value, (six.binary_type, six.text_type)):
            return value

        if typ == "int":
            return int(value)
        elif typ == "bool":
            return value.lower() in {"1", "true", "on", "an", "yes"}
        return value

    def get(self, section, option):
        """get value"""
        return self.config[section][option]["value"]

    def __getitem__(self, section):
        """provides dictonary like access: c['section']['option']"""
        return Section(self, section)


class Section:
    """provides dictionary like access for configparser"""

    #----------------------------------------------------------------------
    def __init__(self, parser, section):
        """Constructor"""
        self.parser = parser
        self.section = section

    #----------------------------------------------------------------------
    def __getitem__(self, item):
        """getitem"""
        return self.parser.get(self.section, item)
