from configs.project_options import ProjectOptions
from configs.configs import Configs
from gateways.env_gateway import EnvGateway
from gateways.file_gateway import FileGateway
from gateways.git_gateway import GitGateway


def main():
    pconfs, lib_opt, env_gate, fgate, git_gate = setup_dependencies()
    pconfs.set_configs()
    lib_opt.load_project_options()
    env_gate.setup_env(pconfs.env_path, pconfs.env_name)


def setup_dependencies():
    proj_configs = Configs()
    lib_options = ProjectOptions()
    env_gateway = EnvGateway()
    fgate = FileGateway()
    git_gate = GitGateway()

    return proj_configs, lib_options, env_gateway, fgate, git_gate
