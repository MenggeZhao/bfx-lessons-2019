## Misc utilities

## Task 1
### Passwordless SSH (10 min)
---

### Instructions
[https://linuxize.com/post/how-to-setup-passwordless-ssh-login/](https://linuxize.com/post/how-to-setup-passwordless-ssh-login/)

### Add bash alias to .bash_profile
```
alias ssr='ssh USER@respublica-an01.research.chop.edu'
alias scv="evansj@refosco.research.chop.edu:"
```
Now in terminal:
```
$ source .bash_profile
```

### Respublica login usage
```
# login to respublica
$ ssr
```

### Copy a file to respublica
```
# copy file to respublica
$ scp some_file.txt $ssr/home/evansj/
```

## Task 2
### Tmux (20 min)
---

### Instructions
* [https://hackernoon.com/a-gentle-introduction-to-tmux-8d784c404340](https://hackernoon.com/a-gentle-introduction-to-tmux-8d784c404340)

### My tmux config (if interested)
* Save as .tmux.conf in /home/USER/
* [config](https://raw.githubusercontent.com/samesense/dotfiles/master/.tmux.conf)

## Cookiecutter tasks
[https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/ll.md](https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/ll.md)
---

## Jupyter notebook tasks
---

### Launch notebook on respublica
[https://wiki.chop.edu/pages/viewpage.action?spaceKey=RISUD&title=%28BETA%29+Jupyter+Notebooks](https://wiki.chop.edu/pages/viewpage.action?spaceKey=RISUD&title=%28BETA%29+Jupyter+Notebooks)

### Install packages in conda env
```
$ jupyter notebook --generate-config
$ conda create -n j_env python=2.7
$ source activate j_env
$ conda install pandas ipykernel
$ python -m ipykernel install --user --name j_env --display-name "j_env"
```

### Jupyter tutorial - Creating A New Notebook
* [https://medium.com/codingthesmartway-com-blog/getting-started-with-jupyter-notebook-for-python-4e7082bd5d46](https://medium.com/codingthesmartway-com-blog/getting-started-with-jupyter-notebook-for-python-4e7082bd5d46)
* try `import pandas`

## Git tasks
---

### Github tutorial
* [https://github.com/samesense/github_tutorial](https://github.com/samesense/github_tutorial)

### Search history for phrase
```
# search all files for touch in diff
# inside github_tutorial
$ git log -Stouch
```

Results:
```
commit eacd4dd0cb97516c41ac8dede737d263b95ffd48 (HEAD -> master, origin/master, origin/HEAD)
Author: Perry <samesense@users.noreply.github.com>
Date:   Fri Apr 5 09:55:31 2019 -0400

    Update README.md
```

Now go to that commit:
```
# checkout commit with first mention of touch
$ git checkout eacd4dd0cb97516c41ac8dede737d263b95ffd48
# return to main branch
$ git checkout master
```

```
# find commit before touch was entered
# top of history is the latest
$ git log README.md | grep -A10 eacd4dd0cb97516c41ac8dede737d263b95ffd48
```

### Search for deleted files
```
# shows when file was in diffs
git log --full-history -- leibyj.txt
```
