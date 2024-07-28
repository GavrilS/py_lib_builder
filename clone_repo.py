import os
from git import Repo


def main(link, path=None):
    if not link and not path:
        print('Either path or link needs to be specified!')
        return
    elif not path:
        path = extract_repo_path_from_link(link)
    
    repo = None
    if os.path.isdir(path):
        repo = Repo(path)
    else:
        repo = Repo.clone_from(link, path)
    
    if repo.bare:
        print('The repo is empty!')
        return
    
    pass



def extract_repo_path_from_link(link):
    path = link.split('/')[-1].replace('.git', '')
    return f"/tmp/{path}"
