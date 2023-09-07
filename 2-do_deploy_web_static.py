#!/usr/bin/python3
"""
Fabric script to deploy an archive to web servers.
"""

from fabric.api import env, put, run, sudo
import os
from os.path import exists

# Define the remote user and hosts
env.user = 'ubuntu'
env.hosts = ['100.24.236.219', '34.229.55.229']

def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the web server
        put(archive_path, '/tmp/')

        # Extract the archive to the /data/web_static/releases/ directory
        archive_filename = os.path.basename(archive_path)
        release_path = '/data/web_static/releases/{}'.format(
            archive_filename[:-4]
        )
        sudo('mkdir -p {}'.format(release_path))
        sudo('tar -xzf /tmp/{} -C {}'.format(archive_filename, release_path))

        # Remove the uploaded archive
        sudo('rm /tmp/{}'.format(archive_filename))

        # Move the contents to a new directory and update permissions
        sudo('mv {}/web_static/* {}'.format(release_path, release_path))
        sudo('rm -rf {}/web_static'.format(release_path))
        sudo('chown -R ubuntu:ubuntu {}'.format(release_path))

        # Update the symbolic link to the new release
        current_link = '/data/web_static/current'
        sudo('rm -rf {}'.format(current_link))
        sudo('ln -s {} {}'.format(release_path, current_link))

        return True
    except Exception as e:
        return False
