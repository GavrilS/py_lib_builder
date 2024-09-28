import sys
import json

REQUIRED_FIELDS = ['name', 'version', 'packages', 'install_requires']
CONF_FILE = 'defaults.json'

class ProjectOptions:

    def __init__(self):
        pass

    @property
    def conf(self):
        return self._conf

    def load_project_options(self, conf=None, conf_file=CONF_FILE):
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

            if not conf_file.endswith('.json'):
                raise Exception('Conf file not properly specified!')
            
            with open(conf_file, 'r') as f:
                conf = json.load(f.readlines()).get('project_options', None)

        conf_verified = self._verify_configs(conf)

        if not conf_verified:
            print('Sorry, the provided configs are wrong or missing needed information!')
            sys.exit(1)

        self._conf = conf

    def _verify_configs(self, conf):
        flag = True
        conf_count = 0
        for key in conf.keys():
            if key in REQUIRED_FIELDS:
                conf_count += 1

        if conf_count < len(REQUIRED_FIELDS):
            return False

        return flag
