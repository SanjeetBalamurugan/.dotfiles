import utils.util as util
import os
import utils.linux as linux
import utils.appimage as appimage
import utils.superuser as superuser

def printDashes(symbol: str) -> None:
    print(os.get_terminal_size().columns)
    return symbol * os.get_terminal_size().columns

def updateRepos(pacman: str) -> None:
    print(printDashes("="))
    print("Updating Repos")
    os.system(f"sudo {pacman} update && sudo {pacman} upgrade")
    print(printDashes("="))


def installPackages(pacman: str) -> None:
    pac = linux.PackageInstaller()
    pac.setPackageManager(pacman)
    pac.addToPackageStack("git")
    pac.addToPackageStack("curl")
    pac.addToPackageStack("wget")
    pac.addToPackageStack("unzip")
    pac.addToPackageStack("vim")
    pac.addToPackageStack("htop")
    pac.installPackages()


def installAppImagePrograms() -> None:
    nvim = appimage.AppImage(
        "https://github.com/neovim/neovim/releases/download/v0.10.0/nvim-linux64.tar.gz",
        "nvim-linux64",
        "nvim",
    )
    nvim.install()


def mainLinux():
    if not util.isInHome():
        print(printDashes("="))
        print("The .dotfiles directory does not exist in the home directory")
        print("Please ensure the .dotfiles directory exists and try again.")
        print(printDashes("="))
        exit(1)

    if not superuser.isInPrivilegedMode():
        print(printDashes("="))
        print("The Python Script Needs To Be In SuperUser Or Admin Mode To Run")
        print("Trying To automatically switch to super user")
        print(printDashes("="))
        superuser.runInPrivilegedMode()

    pacman = util.getPackageManagerLinux()
    print(f"Using Package Manager {pacman}\n\n")
    while True:
        print("Select The Command To Run")
        print("1. Update Repos")
        print("2. Preinstall")
        print("3. Install Programs")
        print("4. Exit Program")
        command = 0
        try:
            command = int(input("\nEnter The Command Number To Run:"))
        except ValueError:
            print("Command Should Be A Number!!\n")
            continue
        if command == 1:
            updateRepos(str(pacman))
        elif command == 2:
            installPackages(str(pacman))
        elif command == 3:
            installAppImagePrograms()
        elif command == 4:
            print("Thanks For Using This Program!!!")
            print(printDashes("="))
            exit(1)
        else:
            print(f"Unknown Command No.: {command}")


if __name__ == "__main__":
    mainLinux()
