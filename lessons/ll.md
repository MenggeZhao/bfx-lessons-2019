## Task 1
### Installation
---

### Setup Miniconda
* [Installing on macOS](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html) optional
```
$ wget https://repo.anaconda.com/miniconda/Miniconda2-latest-MacOSX-x86_64.sh
$ sh Miniconda3-latest-MacOSX-x86_64.sh
```

* respublica: [Install on Linux](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html)
```
$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
$ sh Miniconda3-latest-Linux-x86_64.sh
```

### Install cookiecutter in conda environment
```
$ conda env create -n cookie python=3.5
$ source activate cookie
$ conda install -c conda-forge cookiecutter
$ which cookiecutter
```

## Task 2
### CHOP templates
---

### Setup project structure
```
$ source activate cookie
$ cookiecutter https://github.com/samesense/project-template
# name it demo-project
# examine structure
$ ls -R demo-project
```

### Setup drive structure
```
$ source activate cookie
$ cookiecutter https://github.com/samesense/drive-template
# name it demo-drive
# examine structure
$ ls -R demo-drive
```
