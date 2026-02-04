import git
from git import Repo
git.GIT_PYTHON_GIT_EXECUTE="c:/Program Files/Git/bin/git.exe"

repo = Repo.init("firstrepo")

Repo.clone_from("https://github.com/pratap-singh-chouhan/myfirstrepo.git","myfirstrepo")