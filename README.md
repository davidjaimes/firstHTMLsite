```bash
#!/bin/bash
touch ~/bash_profile
echo '# Author: David Jaimes
# Web: https://djaimes.com
# Email: david@djaimes.com
# Questions: Feel free to contact me about the code.
#
# Custom colors for bash Terminal in OSX
export LSCOLORS=bxgxcxdxbxegedabagacad
export CLICOLOR=1
# Custom bash prompt via kirsle.net/wizards/ps1.html
export PS1="\[$(tput setaf 6)\]djaimes.com \[$(tput setaf 1)\][\W] \[$(tput setaf 6)\]$ \[$(tput sgr0)\]"
# added from http://www.dartmouth.edu/~physics/labs/skycalc/flyer.html
CLASSPATH=$CLASSPATH:~/JSkyCalc
export CLASSPATH
# added by Miniconda3 installer
export PATH="/Users/djaimes/miniconda3/bin:$PATH"
# Collection of aliases for djaimes.com
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
' > ~/bash_profile
# Install Miniconda and Python packages.
# NOTE: Make sure Miniconda shell script is in Downloads folder!
bash ~/Downloads/Miniconda3-latest-MacOSX-x86_64.sh
conda update conda
conda install astropy jupyter matplotlib numpy pandas
conda install -c conda-forge jupyterlab
# Install and configure JSkyCalc
# NOTE: Install java and download .jar file from https://www.dartmouth.edu/~physics/labs/skycalc/flyer.html
mkdir ~/JSkyCalc
mv ~/Downloads/JSkyCalc.jar ~/JSkyCalc/
cd ~/JSkyCalc
jar -xvf JSkyCalc.jar
echo '"Mount Laguna Obs.", 7.76173, 32.84, 8., 1, "Pacific", "P", 1859., 1859.' | cat - ~/JSkyCalc/skycalcsites.dat > temp && mv temp ~/JSkyCalc/skycalcsites.dat
```
