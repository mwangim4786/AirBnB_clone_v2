#!/usr/bin/python3
"""Fabfile to generates a .tgz archive from the contents of web_static.
"""
from fabric.api import *
from os import path
from datetime import datetime

env.hosts = ['54.89.194.112', '54.234.34.132']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'

def do_pack():
    """Function to compress directory

    Return: path to archive on success
    None on fail
    """
    # current time
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    archive_path = 'versions/web_static_' + now + '.tgz'

    # Create archive
    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(archive_path))

    # Check that archiving was successful
    if result.succeeded:
        return archive_path
    return None



def do_deploy(archive_path):
    """Deploy web files to server in file /tmp/
    """
    try:
        if not (path.exists(archive_path)):
            return False

        # upload archive file
        put(archive_path, '/tmp/')

        # create target directory, copy datetime to variable timestamp
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

        # uncompress archive file to set dir. and delete .tgz file
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # remove archive file
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        # move contents into host web_static dir.
        run('sudo mv /data/web_static/releases/web_static_{}/\
web_static/* /data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # remove thw extra web_static dir.
        run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
            .format(timestamp))

        # delete existing symbolic link
        run('sudo rm -rf /data/web_static/current')

        # create new symbolic link
        run('sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
    except:
        return False

    # True on success
    return True



def deploy():
    """Deploy web static
    """
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)

