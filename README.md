```shell
# Custom colors for bash Terminal in OSX
export LSCOLORS=bxgxcxdxbxegedabagacad
export CLICOLOR=1
# Custom bash prompt via kirsle.net/wizards/ps1.html
export PS1="\[$(tput setaf 6)\]djaimes.com \[$(tput setaf 1)\][\W] \[$(tput setaf 6)\]$ \[$(tput sgr0)\]"
# added from https://www.dartmouth.edu/~physics/labs/skycalc/flyer.html
export CLASSPATH=$CLASSPATH:~/JSkyCalc
# added by Miniconda3 installer
export PATH="/Users/djaimes/miniconda3/bin:$PATH"
# Collection of aliases for djaimes.com bash scripting
alias jsky="java JSkyCalc"
alias convert="ipython nbconvert --to latex"
alias jynb="jupyter notebook"
alias jlab="jupyter lab"
alias coffee="caffeinate -u -t"
alias ls="ls -lh"
alias stat="git status"
alias add="git add"
alias com="git commit -m"
alias push="git push"
alias brindle="cd ~/anaconda3/lib/python3.7/site-packages/brindle"
```
