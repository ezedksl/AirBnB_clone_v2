#!/usr/bin/python3
"""With Fabric, creates a .tgz backup of web_static/ contents."""
from fabric import operations as op
import datetime


def do_pack():
    """Packer function (adds creation date to file name)."""
    op.local("mkdir versions &> /dev/null")
    now = datetime.datetime.now()
    version = "{}{}{}{}{}{}".format(now.year, now.month, now.day,
                                    now.hour, now.minute, now.second)
    op.local("tar -cvzf versions/web_static_%s.tgz web_static" % version)
    return "versions/web_static_" + str(version) + ".tgz"
