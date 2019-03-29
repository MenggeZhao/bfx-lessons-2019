## Day 2 Snakemake
* Anaconda hpc 
* Conda env snakemake
* Singularity snakemake 
* Http/ftp
* Box interactions

## Task 1
### Installation (20 min)
---

### Setup Miniconda
* respublica: [Install on Linux](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html)
* [Installing on macOS](https://conda.io/projects/conda/en/latest/user-guide/install/macos.html) optional

### Install snakemake
```
$ conda create -n snakemake-env python=3.7
$ source activate snakemake-env
$ conda install -c bioconda -c conda-forge snakemake
$ which snakemake
```

## Task 2
### Simple Snakefile (30 min)
---

### Creating a fake workspace with FASTQ files
In this example, we will process fake paired-end RNA-seq data from FASTQ files. Our “pipeline” consists of two steps:

* Quantify gene expression from the raw RNA-seq reads.
* Collate the gene expression outputs into one master file.

Let’s get started by creating a workspace with our fake data:

```
$ cd $HOME

# Create a folder where we will run our commands:
$ mkdir snakemake-example
$ cd snakemake-example

# Make a fake genome:
$ touch genome.fa

# Make some fake data:
$ mkdir fastq
$ touch fastq/Sample1.R1.fastq.gz fastq/Sample1.R2.fastq.gz
$ touch fastq/Sample2.R1.fastq.gz fastq/Sample2.R2.fastq.gz
```

### Create Snakefile
Let’s create a file called Snakefile to complete the first step of our pipeline. Open your preferred text editor, paste the code below, and save it into a file called `snakemake-example/Snakefile`.

```
SAMPLES = ['Sample1', 'Sample2']

rule all:
    input:
        expand('{sample}.txt', sample=SAMPLES)

rule quantify_genes:
    input:
        genome = 'genome.fa',
        r1 = 'fastq/{sample}.R1.fastq.gz',
        r2 = 'fastq/{sample}.R2.fastq.gz'
    output:
        '{sample}.txt'
    shell:
        'echo {input.genome} {input.r1} {input.r2} > {output}'
```

### Dryrun the pipeline
```
# if not in env
$ source activate snakemake-env

$ snakemake -s Snakefile -n all
```

### Run the pipeline
```
# if not in env
$ source activate snakemake-env

$ snakemake -s Snakefile -j2 all
```

### Extending the Snakefile to collate output files
Let’s extend our Snakefile to have one more rule. We’ll collate the two output files into one master file that represents all samples.

Here’s the new modified Snakefile. Notice that the final output for our pipeline (specified in the rule all section) is now called test.txt. Also notice that we have a recipe for creating the test.txt file in rule collate_outputs.

```
SAMPLES = ['Sample1', 'Sample2']

rule all:
    input:
        'test.txt'

rule quantify_genes:
    input:
        genome = 'genome.fa',
        r1 = 'fastq/{sample}.R1.fastq.gz',
        r2 = 'fastq/{sample}.R2.fastq.gz'
    output:
        '{sample}.txt'
    shell:
        'echo {input.genome} {input.r1} {input.r2} > {output}'

rule collate_outputs:
    input:
        expand('{sample}.txt', sample=SAMPLES)
    output:
        'test.txt'
    run:
        with open(output[0], 'w') as out:
            for i in input:
                sample = i.split('.')[0]
                for line in open(i):
                    out.write(sample + ' ' + line)
```

### Run the pipeline
```
# if not in env
$ source activate snakemake-env

# dryrun
$ snakemake -s Snakefile -n all

# real run
$ snakemake -s Snakefile -j2 all

# force re-run
snakemake -s Snakefile -j2 -F all
```

### Extending the Snakefile to use regular expression glob strings
Previously, we hard-coded the sample names like this:
```
SAMPLES = ['Sample1', 'Sample2']
```
For real work, we might want to make our Snakefile more flexible by using regular expressions to capture sample names from file names.

Below, we have extended the Snakefile to use regular expression glob strings:
```
from os.path import join

# Globals ---------------------------------------------------------------------

# Full path to a FASTA file.
GENOME = 'genome.fa'

# Full path to a folder that holds all of your FASTQ files.
FASTQ_DIR = './fastq/'

# A Snakemake regular expression matching the forward mate FASTQ files.
SAMPLES, = glob_wildcards(join(FASTQ_DIR, '{sample,Samp[^/]+}.R1.fastq.gz'))

# Patterns for the 1st mate and the 2nd mate using the 'sample' wildcard.
PATTERN_R1 = '{sample}.R1.fastq.gz'
PATTERN_R2 = '{sample}.R2.fastq.gz'

# Rules -----------------------------------------------------------------------

rule all:
    input:
        'test.txt'

rule quantify_genes:
    input:
        genome = GENOME,
        r1 = join(FASTQ_DIR, PATTERN_R1),
        r2 = join(FASTQ_DIR, PATTERN_R2)
    output:
        '{sample}.txt'
    shell:
        'echo {input.genome} {input.r1} {input.r2} > {output}'

rule collate_outputs:
    input:
        expand('{sample}.txt', sample=SAMPLES)
    output:
        'test.txt'
    run:
        with open(output[0], 'w') as out:
            for i in input:
                sample = i.split('.')[0]
                for line in open(i):
                    out.write(sample + ' ' + line)
```

### Run on cluster
```
$ snakemake -s Snakefile --latency-wait 20  -p -j 2 -c "qsub -l h_vmem=1G -l mem_free=1G -l m_mem_free=1G"

# watch jobs
# open new respulica session
$ watch --interval=0.1 qstat
# Use Ctrl-C to stop qstat watch
```

## Task 3
### Containers (10 min)
---

```
from os.path import join

# Globals ---------------------------------------------------------------------

# Full path to a FASTA file.
GENOME = 'genome.fa'

# Full path to a folder that holds all of your FASTQ files.
FASTQ_DIR = './fastq/'

# A Snakemake regular expression matching the forward mate FASTQ files.
SAMPLES, = glob_wildcards(join(FASTQ_DIR, '{sample,Samp[^/]+}.R1.fastq.gz'))

# Patterns for the 1st mate and the 2nd mate using the 'sample' wildcard.
PATTERN_R1 = '{sample}.R1.fastq.gz'
PATTERN_R2 = '{sample}.R2.fastq.gz'

# Rules -----------------------------------------------------------------------

rule all:
    input:
        'test.txt'

rule quantify_genes:
    input:
        genome = GENOME,
        r1 = join(FASTQ_DIR, PATTERN_R1),
        r2 = join(FASTQ_DIR, PATTERN_R2)
    output:
        '{sample}.txt'
    singularity:
        'docker://quay.research.chop.edu/evansj/plink2-docker'
    shell:
        'plink2 --help > {output}
        'echo {input.genome} {input.r1} {input.r2} >> {output}'

rule collate_outputs:
    input:
        expand('{sample}.txt', sample=SAMPLES)
    output:
        'test.txt'
    run:
        with open(output[0], 'w') as out:
            for i in input:
                sample = i.split('.')[0]
                for line in open(i):
                    out.write(sample + ' ' + line)
```

Now run snakemake
```
$ module load singularity
$ snakemake -s Snakefile --latency-wait 20 --use-singularity \
--singularity-args "-B /mnt/isilon/:/mnt/isilon/"\
-p -j 2 -c "qsub -l h_vmem=1G -l mem_free=1G -l m_mem_free=1G" \
all
```
