import sys, optparse, os

import subprocess

if __name__ == '__main__':   

    subprocess.call("python python -m pytest -vv ./system_info.py", shell=True)

    print("Done")