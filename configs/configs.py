import sys
import json

CONF_FILE = 'defaults.json'
ENV_PATH = '/tmp/env/bin/'


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

    def _set_configs(self, conf=None, conf_file=CONF_FILE):
        if not conf:
            count = 0
            end_count = 3
            while True:
                if not conf_file.endswith('.json'):
                    # raise Exception('The configuration file needs to be json formatted!')
                    print(f"The config file provided is not a valid json formatted file! You can enter a new path now. You have {end_count - count} attempts left.")
                    conf_file = input('Please provide the path to the new json config file:')
                    count += 1
                    if count >= end_count:
                        break
                else:
                    break
            
            with open(conf_file, 'r') as f:
                conf = json.load(f.readlines()).get('project_structure', None)
        
        conf_verifier = self._verify_configs(conf)

        if not conf_verifier:
            print('Sorry, the provided configs are wrong or missing needed information!')
            sys.exit(1)
        
        self.project_name = conf.get('project_name')
        self.project_dir = conf.get('project_directory')
        self.project_repo = conf.get('project_repo')
        self.destination = conf.get('destination')
        self.env_path = conf.get('environment_path')
        
    def _verify_configs(self, conf):
        flag = False
        if conf.get('project_name', None) and conf.get('project_directory', None):
            flag = True
        elif conf.get('project_repo', None) and conf.get('destination', None):
            flag = True
        
        return flag and conf.get('environment_path', None)
