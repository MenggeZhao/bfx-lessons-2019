# Day 1 tasks

## Task 1
##### Setup singularity (10min)
---

### Setup lab drive
```
# template: https://github.com/samesense/drive-template
$ mkdir -p /mnt/isilon/some_lab/users/USER/.singularity
```
### Symlink singularity cache
```
# on respublica
$ ln -s /mnt/isilon/some_lab/users/USER/.singularity /home/USER/.singularity

# if ~/.singularity exists, copy content to lab drive space 
# (/mnt/isilon/some_lab/users/USER/.singularity/)
```

### Explore image in singularity
* Locate image on dockerhub, singularity hub, quay, or biocontainers
* Use `shell` to enter image
```
# on respublica
$ module load singularity 
$ singularity shell -B /mnt/isilon/:/mnt/isilon/ docker://maxulysse/samtools:1.0
```
    
* Search or tool execuatable
* Run tool help command
* `cd` to your projects on isilon

## Task 2
##### Quay Dockerfile build (10 min)
---

* Create [CHOP GitHub](https://github.research.chop.edu/) as needed
* [Create CHOP GitHub repo](https://github.research.chop.edu/new) called `test-docker`

### Create a Dockerfile in CHOP GitHub repo
```
################## BASE IMAGE ######################

# https://hub.docker.com/r/biocontainers/biocontainers/dockerfile/
FROM biocontainers/biocontainers:v1.0.0_cv4

################## METADATA ######################

LABEL base_image="biocontainers:v1.0.0_cv4"
LABEL version="3"
LABEL software="bedtools"
LABEL software.version="2.27.0"
LABEL about.summary="a powerful toolset for genome arithmetic"
LABEL about.home="http://bedtools.readthedocs.io/en/latest/"
LABEL about.documentation="http://quinlanlab.org/tutorials/bedtools/bedtools.html"
LABEL about.license_file="https://github.com/arq5x/bedtools2/blob/master/LICENSE"
LABEL about.license="SPDX:LGPL-2.0-only"
LABEL extra.identifiers.biotools="bedtools"
LABEL about.tags="Genomics"

RUN conda install bedtools=2.27.0
```
* [Create quay repo](https://quay.research.chop.edu/new/) called `test-quay` and link to GitHub repo `test-docker`

### Test container
```
# on respublica
$ module load singularity
$ singularity shell -B /mnt/isilon/:/mnt/isilon/ docker://quay.research.chop.edu/{USER}/test-quay
```

## Task 3
##### DockerHub Dockerfile build (10 min)
---

* Create [dockerhub](https://hub.docker.com/) and [github]((https://github.com/) accounts as needed
* [Create GitHub repo](https://github.com/new) called `test-docker`

### Create a Dockerfile in GitHub repo
```
################## BASE IMAGE ######################

# https://hub.docker.com/r/biocontainers/biocontainers/dockerfile/
FROM biocontainers/biocontainers:v1.0.0_cv4

################## METADATA ######################

LABEL base_image="biocontainers:v1.0.0_cv4"
LABEL version="3"
LABEL software="bedtools"
LABEL software.version="2.27.0"
LABEL about.summary="a powerful toolset for genome arithmetic"
LABEL about.home="http://bedtools.readthedocs.io/en/latest/"
LABEL about.documentation="http://quinlanlab.org/tutorials/bedtools/bedtools.html"
LABEL about.license_file="https://github.com/arq5x/bedtools2/blob/master/LICENSE"
LABEL about.license="SPDX:LGPL-2.0-only"
LABEL extra.identifiers.biotools="bedtools"
LABEL about.tags="Genomics"

RUN conda install bedtools=2.27.0
```
* [Create DockerHub automated repo](https://hub.docker.com/) called `test-docker` and link to GitHub repo `test-docker` 

### Test container
```
# on respublica
$ module load singularity
$ singularity shell -B /mnt/isilon/:/mnt/isilon/ docker://{DOCKER-HUB-USER}/test-docker
```

#### Building containers - getting help on github

$SINGULARITY_CACHEDIR
