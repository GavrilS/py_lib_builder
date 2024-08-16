import json

CONF_FILE = 'defaults.json'


class Configs:

    def __init__(self, conf=None, conf_file=CONF_FILE):
        pass

    @property
    def project_name(self):
        return self._project_name
    
    @project_name.setter
    def project_name(self, project_name):
        self._project_name = project_name

    @property
    def project_dir(self):
        return self._project_dir
    
    @project_dir.setter
    def project_dir(self, project_dir):
        self._project_dir = project_dir

    @property
    def project_repo(self):
        return self._project_repo
    
    @project_repo.setter
    def project_repo(self, project_repo):
        self._project_repo = project_repo

    @property
    def destination(self):
        return self._destination
    
    @destination.setter
    def destination(self, destination):
        self._destination = destination
    
    @property
    def env_path(self):
        return self._env_path
    
    @env_path.setter
    def env_path(self, env_path):
        self._env_path = env_path

    def set_configs(self, conf=None, conf_file=CONF_FILE):
        if not conf:
            if not conf_file.endswith('.json'):
                raise Exception('The configuration file needs to be json formatted!')
            
            with open(conf_file, 'r') as f:
                conf = json.load(f.readlines())
        
        
