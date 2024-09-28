import os
from git import Repo

DEFAULT_REPO_DIR = '/tmp/build_package/'

class GitGateway:

    def __init__(self, link, path=None):
        self._link = link
        self._path = path

    def pull_repo(self):
        if not self._verify_repo_configs():
            print('You need to provide a git link to clone the repo from!')
            return None
        
        repo = Repo.clone_from(self.link, self.path)
        
        if repo.bare:
            raise Exception('The provided link is wrong or the repo could not be cloned!')


    def _verify_repo_configs(self):
        return self.link or self.path

    @property
    def link(self):
        return self._link
    
    @property
    def path(self):
        return self._path
