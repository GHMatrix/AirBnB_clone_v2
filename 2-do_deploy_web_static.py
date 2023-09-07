#!/usr/bin/python3
"""Fabric script to distribute an archive
to web servers using do_deploy function."""

from fabric.api import put, run, env
import os

env.hosts = ['100.24.236.219', '34.229.55.229']
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    deploys archive to web server
    """
    path = archive_path.split('/')[-1]
    line = path.split('.')[0]
    if not os.path.isfile(archive_path):
        return False
    if put(archive_path, "/tmp/{}".format(path)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}"
            .format(line)).failed:
        return False
    if run("mkdir -p /data/web_static/releases/{}/"
            .format(line)).failed:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(path, line)).failed:
        return False
    if run("rm /tmp/{}".format(path)).failed:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(line, line)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static"
            .format(line)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(line)).failed:
        return False

    return True
