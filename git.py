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


def get_remote_url(path, remote='origin'):
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


def sync_local_from_remote(origin, branch):
    """Pull all the latest details from a remote to a local repo"""
    # Update the local git database
    run("git fetch")

    # Switch to the right branch
    run("git checkout %s" % branch)

    # Obliterate any local changes
    run("git checkout .")

    # Merge the latest code on this branch
    run('git pull %s %s' % (origin, branch))


def sync_submodules():
    run("git submodule update --init --recursive")
