from subprocess import getoutput


def get_current_branch_name():
    p = getoutput("git branch | grep \\* | cut -d ' ' -f2")
    return p.strip()


def get_base_branch_name():
    p = getoutput(
        "git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@'"
    )
    return p.strip()
