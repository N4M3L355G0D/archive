#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
PS1='\e[1;32;40m[\[\u\e[0m\e[1;31;40m@\e[0m\e[1;33;40m\h\e[0m\e[1;36;40m:\W]\]\$\e[0m '
shopt -s direxpand
export build=$HOME/build
