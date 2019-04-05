---
title: bfx-lessons-day3
verticalSeparator: <!--v-->
theme: solarized
---

# Day 3
* Passwordless SSH
* Terminal multiplexers
* [Cookiecutter](ll.md)
* [Jupyter](jupyter.md)
* [Git](git.md)
---

## Passwordless SSH
* bash alias in `~/.bash_profile`
```
alias ssr1='ssh evansj@respublica-an02.research.chop.edu'
alias scv="evansj@refosco.research.chop.edu:"
```

```
$ ssr
$ scp some_file.txt $ssr/home/evansj/
```
---

## Passwordless SSH
* [Directions](https://linuxize.com/post/how-to-setup-passwordless-ssh-login/)
* [https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day3.md#task-1](https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day3.md#task-1)
---

## Terminal multiplexers
* tmux
* screen 
---

## Default tmux session
```
if [ -z "$TMUX" ]; then
tmux attach -t default || tmux new -s default
fi
```
(in .bash_profile on remote machine)
---

## Tmux prefix 
* prefix: `Ctrl-t` 
```
unbind-key C-b
set -g prefix 'C-t' #
bind-key 'C-t' send-prefix
```
(in .tmux.conf)
---

## Use same respublica head node each login 
```
alias ssr1='ssh evansj@respublica-an01.research.chop.edu'
alias ssr2='ssh evansj@respublica-an02.research.chop.edu'
```
---

## Tmux versions
* respublica: 1.8
* latest: 2.3
---

## Tmux resurrect
* [https://github.com/tmux-plugins/tmux-resurrect](https://github.com/tmux-plugins/tmux-resurrect)
---

## Task 2: tmux 
* [https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day3.md#task-1](https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day3.md#task-2)
---
