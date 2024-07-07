import os, sys, ctypes, platform, pwd


def isInPrivilegedMode() -> bool:
    if platform.system() == "Windows":
        try:
            return bool(ctypes.windll.shell32.IsUserAnAdmin())
        except:
            return False
    elif platform.system() == "Linux":
        return os.geteuid() == 0
    else:
        raise NotImplementedError("Unsupported Platform")


def runInPrivilegedMode() -> bool | None:
    if isInPrivilegedMode():
        return True

    script = os.path.abspath(sys.argv[0])
    params = [script] + sys.argv[1:]

    if platform.system() == "Windows":
        try:
            ctypes.windll.shell32.ShellExecuteW(
                None, "runas", sys.executable, " ".join(params), os.getcwd(), 1
            )
        except Exception as e:
            print(f"Failed To Elevate To Admin: {e}")
    elif platform.system() == "Linux":
        try:
            command = ["sudo", "--preserve-env", sys.executable, " ".join(params)]
            print(" ".join(command))
            os.execvp("sudo", args=command)
        except Exception as e:
            print(f"Failed To Elevate To Admin: {e}")

    sys.exit()
