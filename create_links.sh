#!/bin/bash

DOTFILES=$HOME/.dotfiles

if [[ ! -d "$DOTFILES" ]]; then
  echo "=======  ======="
  echo "The .dotfiles directory does not exist in the home directory."
  echo "Please ensure the .dotfiles directory exists and try again."
  echo "=======  ======="
  exit 1
fi

echo "======= Removing Existing Files ======="
rm -f $HOME/.gitconfig
rm -f $HOME/.bashrc
rm -f $HOME/.profile

echo "======= Removing Folders ======="
rm -rf $HOME/.config

echo "======= Creating SymLinks ======="
ln -s $DOTFILES/.gitconfig $HOME/.gitconfig
ln -s $DOTFILES/.bashrc $HOME/.bashrc
ln -s $DOTFILES/.profile $HOME/.profile
ln -s $DOTFILES/.config $HOME/.config
