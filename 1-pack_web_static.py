#!/usr/bin/python3
"""Fabric script to generate a .tgz archive from
the contents of the web_static folder."""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Path to the archive if successful, None otherwise.
    """
    try:
        # Create the 'versions' directory if it doesn't exist
        local("mkdir -p versions")

        # Create the archive name using the current date and time
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_{}.tgz".format(current_time)

        # Compress the contents of the 'web_static' directory into the archive
        local("tar -czvf {} web_static".format(archive_name))

        # Check if the archive has been created successfully
        if local("test -e {}".format(archive_name)).succeeded:
            return archive_name

        return None
    except Exception as e:
        return None
