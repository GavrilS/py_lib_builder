from subprocess import Popen, PIPE

class LibraryHandler:

    def __init__(self, local_env, project_parent_dir):
        self._local_env = local_env
        self._project_dir = project_parent_dir 
    
    @property
    def local_env(self):
        return self._local_env
    
    @property
    def project_dir(self):
        return self._project_dir

    def run_install_command(self):
        activate_env_cmd = ['source', f"{self.local_env}/bin/activate"]
        proc = Popen(activate_env_cmd, stdout=PIPE, stderr=PIPE)
        res = proc.wait(timeout=30)
        print('Activate cmd res: ', res)

        install_lib_cmd = ['pip3', 'install', f"{self.project_dir}"]
        proc = Popen(install_lib_cmd, stdout=PIPE, stderr=PIPE)
        res = proc.wait(timeout=300)
        print('Install lib response: ', res)

        deactivate_env_cmd = ['deactivate']
        proc = Popen(deactivate_env_cmd)
        res = proc.wait(timeout=30)
        print('Deactivate command res: ', res)
