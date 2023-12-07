#!/usr/bin/python3
"""Fabfile to generates a .tgz archive from the contents of web_static.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Function to compress directory

    Return: path to archive on success
    None on fail
    """
    # current time
    now = datetime.now()
    now = now.strftime('%Y%m%d%H%M%S')
    arch_path = 'versions/web_static_' + now + '.tgz'

    # Create archive
    local('mkdir -p versions/')
    result = local('tar -cvzf {} web_static/'.format(arch_path))

    # Check that archiving was successful
    if result.succeeded:
        return arch_path
    return None
