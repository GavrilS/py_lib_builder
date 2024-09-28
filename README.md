# py_lib_builder

A project to set up and install python custom-build libraries.

# Project steps:

- pull a project from git or verify we have one set up already
- build the package and install it with pip

# Config files

This project works with a config file that provides the necessary settings for it to function properly. You can use the 'default.json' file under the 'configs' directory. The file should have the following structure: a json object with 2 json objects inside it - "project_structure" and "project_options".

- project_structure should contain the following fields:

  - project_name - this is the source of the installed library(this includes the path from within the parent directory)(STRING)
  - project_directory - this is the path to the parent directory, where the source lives(STRING)
  - project_repo - this needs to include a link to the git project in case the project is not cloned on the local machine(STRING)
  - destination - this is the place where the source for the library will be moved for the setup and installation steps(STRING)
  - environment_path - the path to the virtual environment(STRING)
  - environment_name - the name of the virtual environment folder(STRING)

- project_options should contain the following fields:
  - name - the name of the library we want to install(STRING)
  - version - the version in the format "0.1.0"(STRING)
  - packages - the module packages; if the source folder is called 'example' and you want to include everything from within it, the packages will look like this: ["example", "example.\*"](LIST)
  - install_requires - any required libraries which are used in the custom module(LIST)
