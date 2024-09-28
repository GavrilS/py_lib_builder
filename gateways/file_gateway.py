import os
from subprocess import Popen, PIPE


class FileGateway:

    def __init__(self):
        pass

    def create_setup_file(path, file, content):
        with open(f"{path}/{file}", 'w') as f:
            f.write(content)

    def verify_project_exists(self, project_path):
        return os.isdir(project_path)

    def copy_project_to_work_dir(project_src, work_dir):
        # cmd = f"mv -rf {project_src} {work_dir}"
        cmd = ['mv', '-rf', project_src, work_dir]

        ps = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = ps.communicate()
        print('Output of the "copy_project_to_work_dir" command: ', stdout)
        print('Errors resulting from the command: ', stderr)

    def clear_work_dir(work_dir):
        cmd = ['rm', '-rf', work_dir]

        ps = Popen(cmd, stdout=PIPE, stderr=PIPE)
        stdout, stderr = ps.communicate()
        print('Output of the "clean_work_dir" command: ', stdout)
        print('Errors resulting from the command: ', stderr)
