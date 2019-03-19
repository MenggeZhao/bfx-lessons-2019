### Day1

#### What are containers?

#### Why containers?
* cattle not pets

#### Searching Dockerhub

#### Searching Biocontainers

#### Running Singularity

#### Task 0: Setup lab drive (5min)
```
# template: https://github.com/samesense/drive-template
$ mkdir -p /mnt/isilon/some_lab/users/USER/.singularity
```

#### Task 1: Setup singularity (5min)
    ```
    # on respublica
    $ ln -s /mnt/isilon/some_lab/users/USER/.singularity /home/USER/.singularity
    
    # if ~/.singularity exists, copy content to lab drive space (/mnt/isilon/some_lab/users/USER/.singularity/)
    ```

#### Task 2: Explore image in singularity (10min)
    * Setup singularity 
    * Locate image on dockerhub, singularity hub, quay, or biocontainers
    * Use `shell` to enter image
    ```
    # on respublica
    $ module load singularity 
    $ singularity shell docker:maxulysse/samtools:1.0
    ```
    
    * Search or tool execuatable
    * Run tool help command
    * `cd` to your projects on isilon

#### Task 3: Update image (5 min)
```
$ singularity build --sandbox /tmp/debian docker://debian:latest
$ sudo singularity exec --writable /tmp/debian apt-get install python
$ singularity build /tmp/debian2.simg /tmp/debian
```

#### Task 4: Simple Dockerfile (5 min)

#### Task 5: Automate dockerhub builds (10 min)

#### Task 6: Automate quay builds (10 min)

#### Building containers - getting help on github

#### Building containers - Dockerfile

#### Building containers - dockerhub

#### Building containers - quay

* Anaconda in container
* Scif
