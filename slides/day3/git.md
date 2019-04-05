---
title: bfx-lessons-day3
verticalSeparator: <!--v-->
theme: solarized
---

# Git

* [github.research.chop.edu/](github.research.chop.edu/) 
* Keep track of tasks/assignments
* Reproduce old results
* Lab notebook for each project
---

## Requests as issues
* demo
* [https://github.com/samesense/github_tutorial/blob/master/README.md#07-create-an-issue](https://github.com/samesense/github_tutorial/blob/master/README.md#07-create-an-issue)
---

## Smart rendering
* [jupyter](https://github.research.chop.edu/Hayerk/jupyter_notebooks/blob/master/box_plots_m6a.ipynb)
* [tables](https://github.com/samesense/ibd-gwas/blob/master/writeup/tables/prs.eur.md)
---

## Search history for phrase
```
# search all files for touch in diff
git log -Stouch
```

```
commit eacd4dd0cb97516c41ac8dede737d263b95ffd48 (HEAD -> master, origin/master, origin/HEAD)
Author: Perry <samesense@users.noreply.github.com>
Date:   Fri Apr 5 09:55:31 2019 -0400

    Update README.md
```

```
# checkout commit with first mention of touch
git checkout eacd4dd0cb97516c41ac8dede737d263b95ffd48
# return to main branch
git checkout master
```

```
# find commit before touch was entered
# top of history is the latest
git log README.md | grep -A10 eacd4dd0cb97516c41ac8dede737d263b95ffd48
```
---

## Search for deleted files
```
# shows when file was in diff
git log --full-history -- leibyj.txt
```
---

## Branching?
---
