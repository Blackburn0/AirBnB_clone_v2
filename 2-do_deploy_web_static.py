#!/usr/bin/python3
"""Helps compress the files into a .tgz archive file"""
from datetime import datetime
from fabric.api import *
import os

env.hosts = ['54.173.191.2', '52.86.38.179']
env.user = 'ubuntu'


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


def do_deploy(archive_path):
    """Deploys the compressed static files to both web servers."""
    if os.path.exists(archive_path):
        filename = archive_path.split('/')[1].split('.')[0]
        releases = '/data/web_static/releases'
        put(archive_path, '/tmp/')
        run('mkdir -p {}/{}'.format(releases, filename))
        run('tar -xzf /tmp/{}.tgz -C {}/{}'
            .format(filename, releases, filename))
        run('rm -f /tmp/{}.tgz'.format(filename))
        run('mv {}/{}/web_static/* {}/{}/'.format(releases, filename,
            releases, filename))
        run('rm -rf {}/{}/web_static'.format(releases, filename))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/{} /data/web_static/current'
            .format(releases, filename))
        return True
    else:
        return False
