### Day1

#### What are containers?

#### Why containers?
* cattle not pets

#### Searching Dockerhub

#### Searching Biocontainers

#### Running Singularity

#### Task 0: Setup lab drive
```
$ mkdir -p /mnt/isilon/some_lab/users/USER/.singularity
```

#### Task 1: Setup singularity
    * Symlink singularity cache
    ```
    # on respublica
    $ ln -s /mnt/isilon/some_lab/users/USER/.singularity ./.singularity
    
    # if ~/.singularity exists, copy content to lab drive space (/mnt/isilon/some_lab/users/USER/.singularity/)
    ```

#### Task 2: Explore image in singularity
    * Setup singularity 
    * Locate image on dockerhub, singularity hub, quay, or biocontainers
    * Use `shell` to enter image
    ```
    # on respublica
    module load singularity 
    singularity shell docker:maxulysse/samtools:1.0
    ```
    
    * Search or tool execuatable
    * `cd` to your projects on isilon

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
