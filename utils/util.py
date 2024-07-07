import os
from subprocess import DEVNULL, STDOUT, check_call


def isInHome() -> bool:
    currDir = os.getcwd()
    homePath = os.environ["HOME"]

    if isUnix():
        ps = "/".join(currDir.split("/")[:-1:])
        if homePath == ps:
            return True

    print(f"UTIL:{currDir}\n{homePath}")

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
