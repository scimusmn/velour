from fabric.api import (local)


def get_remote_origin():
    """Return a string of the remote origin URL"""

    # Next step here is to strip out only the URL that we want
    origin = local('git remote show origin')

    return origin
