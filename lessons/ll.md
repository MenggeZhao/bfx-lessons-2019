# Cookiecutter lunch and learn

[Slides](../slides/ll/ll.md)

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

## Task 3
### Edit CHOP template
---

### Fork CHOP project template
* https://github.com/samesense/project-template

### Add .gitkeep file to new folder
* Create new folder under `{{ cookiecutter.repo_name }}`

### Setup project structure with new template
```
$ source activate cookie
$ cookiecutter <YOUR_FORK>
# name it demo-project-2
# examine structure
$ ls -R demo-project-2
```
