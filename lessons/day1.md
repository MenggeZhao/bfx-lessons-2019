### Day1

#### Searching Dockerhub

#### Searching Biocontainers

#### Running Singularity

#### Building containers - testing
```
$ singularity build --sandbox /tmp/debian docker://debian:latest
$ sudo singularity exec --writable /tmp/debian apt-get install python
$ singularity build /tmp/debian2.simg /tmp/debian
```

#### Building containers - getting help on github

#### Building containers - Dockerfile

#### Building containers - dockerhub

#### Building containers - quay

* Anaconda in container
* Scif
