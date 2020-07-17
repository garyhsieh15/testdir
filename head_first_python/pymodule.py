import sys
import os

# ---------------------------------------------------------
# get which os via sys module, sys.platform attribute.
#
# ---------------------------------------------------------
def get_os_system():
    os = sys.platform

    return os
# ---------------------------------------------------------
# get version of python via sys module, sys.version
# attribute.
#
# ---------------------------------------------------------
def get_python_version():
    ver = sys.version

    return ver

# ---------------------------------------------------------
# get current fold's path via os module, os.getcwd()
# function.
#
# ---------------------------------------------------------
def get_current_path():
    curpath = os.getcwd()

    return curpath

# ---------------------------------------------------------
# get environment data via os moduel, os.environ attribute.
#
# ---------------------------------------------------------
def get_env_data():
    env = os.environ

    return env

if __name__ == "__main__":

    os_name = get_os_system()
    ver_python = get_python_version()
    # curpath = get_current_path()
    # env = get_env_data()

    print("type of os: ", os_name)
    print("python version: ", ver_python)
    #print("current paht: ", curpath)
    print("environment: ", os.environ)
