#!/bin/bash

set -e
echo "Using $SHELL"

# Package manager to use
PKG_MGR="apt"

DOTFILES=$HOME/.dotfiles
PKG_INSTALL=$DOTFILES/.app_installs

if [[ ! -d "$DOTFILES" ]]; then
  echo "=======  ======="
  echo "The .dotfiles directory does not exist in the home directory."
  echo "Please ensure the .dotfiles directory exists and try again."
  echo "=======  ======="
  exit 1
fi

check_package_mgr() {
    if command -v "$1" &> /dev/null
    then
      PKG_MGR=$1
      echo "======= Using Package manager $PKG_MGR ======="
    else
        echo "======= $1 is not the package manager for this system ======="
    fi
}

check_package_mgr apt
check_package_mgr dnf
check_package_mgr pacman
check_package_mgr emerge

echo "======== Updating the repos =========="
sudo $PKG_MGR update
sudo $PKG_MGR upgrade

echo "======= Installing Programs Using $PKG_MGR ======="
sudo $PKG_MGR install git curl wget unzip vim

echo "======= Installing .appimage Packages ======="
mkdir -p $PKG_INSTALL

sudo rm -f /usr/bin/nvim
wget https://github.com/neovim/neovim/releases/download/v0.10.0/nvim-linux64.tar.gz -O $PKG_INSTALL/nvim-linux64.tar.gz
sudo tar -xzvf nvim-linux64.tar.gz -C /opt/
sudo ln -s /opt/nvim-linux64/bin/nvim /usr/bin/nvim
