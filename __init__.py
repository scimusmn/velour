from fabric.api import (cd, run)


def get_remote(path, remote='origin'):
    """Return a string of the remote origin URL

    Args:
        path: Directory path to the local repository
        remote: Name of the remote (default = 'origin')

    Returns:
        String containing the git URL of the origin
    """

    with cd(path):
        origin = run('git config --get remote.%s.url' % remote)
        return origin
