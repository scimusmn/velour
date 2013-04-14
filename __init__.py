from fabric.api import (cd, local)


def get_remote_origin(path, remote='origin'):
    """Return a string of the remote origin URL

    Args:
        path: Directory path to the local repository
        remote: Name of the remote (default = 'origin')

    Returns:
        String containing the git URL of the origin
    """

    with cd(path):
        origin = local('git config --get remote.%s.url' % remote)
        return origin
