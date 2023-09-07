#!/usr/bin/python3
"""Fabric script to distribute an archive
to web servers using do_deploy function."""

from fabric.api import local, put, run, env
from os.path import exists

env.hosts = ['<228879-web-01>', '<228879-web-02>']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """
    Distribute an archive to web servers and deploy.

    Args:
        archive_path (str): Path to the archive to be deployed.

    Returns:
        bool: True if all operations have been done correctly, False otherwise.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to /tmp/ directory on the server
        put(archive_path, "/tmp/")

        # Get the base name of the archive
        archive_base = archive_path.split("/")[-1]

        # Define release directory path
        release_dir = "/data/web_static/releases/{}/".format(
                archive_base.split(".")[0])

        # Create the release directory
        run("mkdir -p {}".format(release_dir))

        # Uncompress the archive to the release directory
        run("tar -xzf /tmp/{} -C {}".format(archive_base, release_dir))

        # Remove the archive from the server
        run("rm /tmp/{}".format(archive_base))

        # Remove the current symbolic link
        run("rm -f /data/web_static/current")

        # Create a new symbolic link linked to the new version
        run("ln -s {} /data/web_static/current".format(release_dir))

        return True

    except Exception:
        return False
