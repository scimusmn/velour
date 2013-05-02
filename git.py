from fabric.api import (cd, run)


def check_git(path):
    """Check to see if a path is a Git repository

    Args:
        path: Directory path to check

    Returns:
        Boolean, True if it is a Git repo
    """
    with cd(path):
        result = run('git status')
        if result.return_code != 0:
            return False
        else:
            return True


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
