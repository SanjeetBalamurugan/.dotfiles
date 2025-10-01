import os
from subprocess import DEVNULL, STDOUT, check_call


import os

def isInHome() -> bool:
    currDir = os.getcwd()
    homePath = os.environ.get("HOME", "")

    if os.name == "posix":
        parentDir = os.path.dirname(currDir)
        
        if os.path.realpath(homePath) == os.path.realpath(parentDir):
            return True

    print(f"UTIL: {currDir}\nHOME: {homePath}")

    return False


def getPackageManagerLinux() -> str | None:
    pacmanagers = ["apt", "dnf", "pacman"]

    for p in pacmanagers:
        # if os.system(f"{p} --version") == 0:
        #   return p

        try:
            check_call([p, "--version"], stdout=DEVNULL)
            return p
        except FileNotFoundError:
            continue

    return None


def isUnix() -> bool:
    if os.name == "posix":
        return True
