import os
from git import Repo

class GitGateway:

    def __init__(self, link, path):
        self.link = link
        self.path = path

    def pull_repo(self, link, path=None):
        if not self._verify_repo_configs():
            print('You need to provide either a path to an existing repo or a git link to clone the repo from!')
            return None
        
        repo = None
        if os.path.isdir(path):
            repo = Repo(path)
        else:
            repo = Repo.clone_from(link, path)
        
        if repo.bare:
            print('The provided repo is empty!')
            return None
        
        return path
        
    def _extract_repo_path_from_link(self, link):
        path = link.split('/')[-1].replace('.git', '')
        return f"/tmp/{path}"

    def _verify_repo_configs(self):
        return self.link or self.path

    @property
    def link(self):
        return self._link
    
    @link.setter
    def link(self, link):
        self._link = link
    
    @property
    def path(self):
        return self._path
    
    @path.setter
    def path(self, path):
        self._path = path
