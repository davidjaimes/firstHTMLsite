## .bash_profile
```shell
# Custom colors for bash Terminal in macOS
# Default is:  “exfxcxdxbxegedabagacad”
export LSCOLORS=gxgxcxdxbxegedabagacad
export CLICOLOR=1
# Custom colored bash prompt
C0="\e[38;5;120m\]"  # Light Green
C1="\e[38;5;227m\]"  # Light Yellow
export PS1="\[$C0\u.com [\[\e[0m\]\[$C1\W\[\e[0m\]\[$C0] $ \[\e[0m\]"
# added from https://www.dartmouth.edu/~physics/labs/skycalc/flyer.html
export CLASSPATH=$CLASSPATH:~/JSkyCalc
# added by Miniconda3 installer
export PATH="/Users/djaimes/miniconda3/bin:$PATH"
# Collection of aliases for djaimes.com bash commands
alias jsky="java JSkyCalc"
alias convert="ipython nbconvert --to latex"
alias jynb="jupyter notebook"
alias jlab="jupyter lab"
alias coffee="caffeinate -u -t"
alias ls="ls"
alias stat="git status"
alias add="git add"
alias com="git commit -m"
alias push="git push"
alias brindle="cd ~/anaconda3/lib/python3.7/site-packages/brindle"
```

## Conda
Turn off the base parenthases on the terminal print out to screen... annoying!
```bash
conda config --set changeps1 false
```

Packages to install:
```
conda astropy jupyter matplotlib numpy pandas scipy
```
