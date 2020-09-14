import sys
import os
import datetime, time


# ---------------------------------------------------------
# get which os via sys module, sys.platform attribute.
#
# ---------------------------------------------------------
def get_os_system():
    os_name = sys.platform

    return os_name

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
    env_data = os.environ

    return env_data

# ---------------------------------------------------------
# get environment item via os moduelm os.getenv()
#
# ---------------------------------------------------------
def get_environ_item():
    print(" ========================================================= ")
    print("    TERM_PROGRAM: ", os.getenv("TERM_PROGRAM"))
    print("    TERM: ", os.getenv("TERM"))
    print("    SHELL: ", os.getenv("SHELL"))
    print("    MYVIMRC: ", os.getenv("MYVIMRC"))
    print("    TMPDIR: ", os.getenv("TMPDIR"))
    print("    PYTHON_PATH: ", os.getenv("PYTHON_PATH"))
    print("    TERM_PROGRAM_VERSION: ", os.getenv("TERM_PROGRAM_VERSION"))

    print("    HOME: ", os.getenv("HOME"))
    print("    LOGNAME: ", os.getenv("LOGNAME"))
    print("    VIMRUNTIME: ", os.getenv("VIMRUNTIME"))
    print("    VIM: ", os.getenv("VIM"))
    print(" ========================================================= ")

# ---------------------------------------------------------
# get time now via datetime and time module, 
# datetime.date.isoformat(), time.strftime().
# 
# ---------------------------------------------------------
def get_time():
    date_month_year = datetime.date.isoformat(datetime.date.today())
    hour_mim = time.strftime("%H:%M")
    week = time.strftime("%A %p")

    return date_month_year, hour_mim, week

if __name__ == "__main__":

    os_name = get_os_system()
    # os = get_os_system()
    ver_python = get_python_version()
    curpath = get_current_path()    
    env_data = get_env_data()

    dmy, hm, w = get_time()

    print("sys.platfom: ", os_name)
    # print("sys.platfom: ", os)
    print("sys.version: ", ver_python)

    print("os.environ: ", env_data)
    print("show env item:") 
    get_environ_item()
    # get_environ_item()
    print("os.getcwd(): ", curpath)
    print("time: ", dmy, hm, w)
