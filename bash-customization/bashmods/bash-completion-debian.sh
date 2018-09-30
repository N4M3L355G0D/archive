if ! shopt -oq posix; then
  if [ -f /usr/share/bash-completion/bash_completion ]; then
    . /usr/share/bash-completion/bash_completion
  elif [ -f /etc/bash_completion ]; then
    . /etc/bash_completion
  fi
fi

HISTSIZE=1000
HISTFILESIZE=2000

shopt -s histappend
shopt -s direxpand
shopt -s checkwinsize

alias ll='ls -l'
alias la='ls -A'
alias l='ls -CF'

grep='grep --color=auto'
egrep='egrep --color=auto'
fgrep='fgrep --color=auto'
