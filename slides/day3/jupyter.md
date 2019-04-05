---
title: bfx-lessons-day3
verticalSeparator: <!--v-->
theme: solarized
---

# Jupyter notebooks
* Experiment with code on respublica
* No need to copy data locally 
* Supports R, julia, python
* Custom anaconda envs
---

## Starting a notebook
[https://wiki.chop.edu/pages/viewpage.action?spaceKey=RISUD&title=%28BETA%29+Jupyter+Notebooks](https://wiki.chop.edu/pages/viewpage.action?spaceKey=RISUD&title=%28BETA%29+Jupyter+Notebooks)
---

## Setup conda env 
```
$ conda create -n j_env python=2.7
$ source activate j_env
$ conda install pandas ipykernel
$ python -m ipykernel install --user --name j_env --display-name "j_env" 
```
---

## Do not pip/conda install from notebooks
```
!pip install pandas
```
---

## Shell magic
```
!ls /mnt/isilon
```
---

## R kernels :(
* gcc issues
---
