---
title: bfx-lessons
verticalSeparator: <!--v-->
theme: solarized
---

# My workflow
* [project template](https://github.com/samesense/project-template)
* GitHub logs everything but data
* snakemake pipeline
* tools from containers or anaconda
* Mostly python, R plots
* Jupyter for POC/testing 
* automate everything 
* prefer multi-core machines, not respublica 

<!--v-->

# Lessons Spring 2019
* containers
* snakemake
* misc utilities
* cwl/cavatica

<!--v-->

## Purpose
* Eliminate tool installations
* Develop disposable and reproducible analysis workflows
* Demo tools/concepts that save time / reduce anger

<!--v-->

![cat](images/anger.png)

<!--v-->
## Comments 
[https://github.com/samesense/bfx-lessons-2019/issues](https://github.com/samesense/bfx-lessons-2019/issues)

---

# Day 1 containers

![cat](sub/cat.jpg)

---

## Containers
* Portable tool and environment
* Installation free
* Easy incorporation into workflow managers
* [https://quay.research.chop.edu/repository/](https://quay.research.chop.edu/repository/evansj/plink2-docker)
```
singularity shell \
docker://quay.research.chop.edu/evansj/plink2-docker
```

<!--v-->

## Why containers?
* Cattle not pets
* Maintenence weekends - nothing breaks after OS/tool chain upgrades
* Suffer tool installations once
* Let others suffer tool installations for you
* No tool/library maintenence
* Easily share your methods

<!--v-->

## Why not respublica modules?
* Modules are not portable
* Module-install lag time
* Spare JD's time 

<!--v-->

## Why not env manager?
* Env managers can fail with complex installs
* Env managers do not play well with all workflow managers
* Save envs for simple tools
* Envs can break after OS/tools chain changes

---

## Where can I get containers? 
* [https://hub.docker.com](https://hub.docker.com)
* [https://biocontainers.pro/#/registry](https://biocontainers.pro/#/registry)
* [https://singularity-hub.org/collections](https://singularity-hub.org/collections)
* [https://quay.research.chop.edu/repository/](https://quay.research.chop.edu/repository/)
* google `tool docker image`

<!--v-->

## How can I use containers? 
* [https://hub.docker.com](https://hub.docker.com)
 ```
 singularity shell docker://samesense/plink-docker:latest
 ```
* [https://biocontainers.pro/#/registry](https://biocontainers.pro/#/registry)
```
singularity shell docker://quay.io/biocontainers/plink:1.90b4--h0a6d026_2
```
* [https://singularity-hub.org/collections](https://singularity-hub.org/collections)
```
singularity shell shub://qbicsoftware/qbic-singularity-snpeff
```
* [https://quay.research.chop.edu/repository/](https://quay.research.chop.edu/repository/)
```
singularity shell docker://quay.research.chop.edu/evansj/prsice-docker
```

<!--v-->

## How can I use containers with data? 
![types-of-mounts-volume](images/types-of-mounts-volume.png)

<!--v-->

## How can I use containers with data? 
 ```
singularity shell -B /mnt/isilon/:/mnt/isilon/ \
docker://samesense/plink-docker:latest
 ```

---

## Docker vs singularity
* Docker root access scares admins - no docker on data machines
* Singularity does not *easily* run on mac
* Docker runs on mac, but uses too much disk space
* Singularity runs on respublica
* Docker and singularity hacks for windows

---

## Task 1: setup singularity
* [https://github.com/samesense/drive-template](https://github.com/samesense/drive-template)
* [https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day1.md#task-1](https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day1.md#task-1)

---

## How do I modify a container?
* Quick way: docker on mac
* Maintainable: `Dockerfile`
 
<!--v-->

## Dockerfile
* Instructions for tool installation
* Inherit config for base image
* [https://github.research.chop.edu/BiG/bfx-docker/blob/master/mega2__v5.0.1/Dockerfile](https://github.research.chop.edu/BiG/bfx-docker/blob/master/mega2__v5.0.1/Dockerfile)
 
<!--v-->

## Dockerfile keywords
* [FROM](https://github.research.chop.edu/BiG/bfx-docker/blob/master/mega2__v5.0.1/Dockerfile#L1)
* [RUN](https://github.research.chop.edu/BiG/bfx-docker/blob/master/mega2__v5.0.1/Dockerfile#L6)
* [ADD](https://github.research.chop.edu/BiG/bfx-docker/blob/master/mega2__v5.0.1/Dockerfile#L3) works with URL or file in Dockerfile dir
* [ENV](https://github.research.chop.edu/BiG/bfx-docker/blob/f13702b866510a91ef1de10b0ec25d0fdb62f084/snpeff__v4.3t/Dockerfile#L54)

<!--v-->

## Building containers from Dockerfile
* Trade-offs for CHOP users
* No singularity on mac
* Docker is mac space hog
* Singularity builds and containers on respublica require root
* Fast solution [https://quay.research.chop.edu/repository/](https://quay.research.chop.edu/repository/)

<!--v-->

## Automated Dockerfile builds
* [https://hub.docker.com](https://hub.docker.com)
* [https://quay.research.chop.edu/repository/](https://quay.research.chop.edu/repository/)

<!--v-->

## Task 2: Quay Dockerfile build
* [https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day1.md#task-2](https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day1.md#task-2)
<!--v-->

## Dockerfile tips
* DO `RUN apt-get update`
* [DO](https://github.research.chop.edu/BiG/bfx-docker/blob/master/mega2__v5.0.1/Dockerfile#L6) `RUN apt-get install -y`
* DONT `RUN cd` alone
* [DO](https://github.research.chop.edu/BiG/bfx-docker/blob/master/mega2__v5.0.1/Dockerfile#L14) `RUN cd dir && command`
* [DO](https://github.research.chop.edu/BiG/bfx-docker/blob/master/mega2__v5.0.1/Dockerfile#L4) `Install R libs from script`
* DO set `$SINGULARITY_CACHEDIR` when disk space is low

<!--v-->

## Dockerfile recommendations
* [https://f1000research.com/articles/7-742/v1](https://f1000research.com/articles/7-742/v1)
* Use a package manager and specify tool version
* One tool per container
* So not store data in container, keep them small
* Put tool in PATH
* Building containers - get inspiration on github

<!--v-->

## Task 3: DockerHub Dockerfile build
* [https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day1.md#task-3](https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day1.md#task-3)

---

## Docker on mac
* Remove disk image file to free space
```
rm ~/Library/Containers/com.docker.docker/Data/vms/0/Docker.qcow2
```
* Modify containers locally
* Build containers locally

<!--v-->

## Task 4: Modify container on mac
* [https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day1.md#task-4](https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day1.md#task-4)

<!--v-->

## Task 5: Build container on mac
* [https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day1.md#task-5](https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day1.md#task-5)

<!--v-->

## Free space
```
docker rm $(docker ps -q -f status=exited)
```

```
docker system prune
```

```
docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
```

---

* Next time: use containers in workflows: snakemake
* Comments [https://github.com/samesense/bfx-lessons-2019/issues](https://github.com/samesense/bfx-lessons-2019/issues)
