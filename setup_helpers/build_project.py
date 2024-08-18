import os
from subprocess import Popen, PIPE


def copy_project_to_work_dir(project_src, work_dir):
    # cmd = f"mv -rf {project_src} {work_dir}"
    cmd = ['mv', '-rf', project_src, work_dir]

    ps = Popen(cmd, stdout=PIPE, stderr=PIPE)
