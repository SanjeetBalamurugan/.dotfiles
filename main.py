import utils.util as util
import os
import utils.linux as linux
import utils.appimage as appimage
import utils.superuser as superuser

def mainLinux():
  if not util.isInHome():
    print("="*60)
    print("The .dotfiles directory does not exist in the home directory")
    print("Please ensure the .dotfiles directory exists and try again.")
    print("="*60)
    exit(1)
  
  if not superuser.isInPrivilegedMode():
    print("="*63)
    print("The Python Script Needs To Be In SuperUser Or Admin Mode To Run")
    print("Trying To automatically switch to super user")
    print("="*63 + "\n")
    superuser.runInPrivilegedMode()

  pacman = util.getPackageManagerLinux()
  print(f"Using Package Manager {pacman}\n\n")
  # print("="*60)
  # print("Updating Repos")
  # os.system(f"sudo {pacman} update && sudo {pacman} upgrade")
  # print("="*60)

  # pac = linux.PackageInstaller()
  # pac.setPackageManager(str(pacman))
  # pac.addToPackageStack("git")
  # pac.addToPackageStack("curl")
  # pac.addToPackageStack("wget")
  # pac.addToPackageStack("unzip")
  # pac.addToPackageStack("vim")
  # pac.addToPackageStack("htop")
  # pac.installPackages()

  nvim = appimage.AppImage("https://github.com/neovim/neovim/releases/download/v0.10.0/nvim-linux64.tar.gz",
                           "nvim-linux64", "nvim")
  nvim.install()

if __name__ == "__main__":
  mainLinux()