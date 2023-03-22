#!/usr/bin/python3
"""Helps compress the files into a .tgz archive file"""
from datetime import datetime
from fabric.api import *
import os


def do_pack():
    """Compresses the web static files"""
    if not os.path.exists('versions'):
        os.makedirs('versions')
    stamp = datetime.now().isoformat().split('.')[0].replace('-', '')\
        .replace('T', '').replace(':', '')
    status = local('tar -czvf versions/web_static_{}.tgz web_static'
                   .format(stamp))
    if status.succeeded:
        return os.path.normpath('versions/web_static_{}.tgz'.format(stamp))
    else:
        return
