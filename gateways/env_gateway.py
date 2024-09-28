import os
from subprocess import Popen, PIPE

DEFAULT_ENV_PATH = '/tmp/'
DEFAULT_ENV_NAME = 'env'

class EnvGateway:

    def __init__(self):
        pass

    def _check_for_existing_env(self, env_path=DEFAULT_ENV_PATH, env_name=DEFAULT_ENV_NAME):
        return os.isdir(f"{env_path}{env_name}")

    def setup_env(self, env_path=DEFAULT_ENV_PATH, env_name=DEFAULT_ENV_NAME):
        if not self._check_for_existing_env(env_path, env_name):
            cmd = ['python3', '-m', 'venv', f"{env_path}{env_name}"]

            proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
            resp = proc.wait(timeout=300)
            print('Creating a new virtual environment: ', resp)
        else:
            print('Virtual environment exists!')
