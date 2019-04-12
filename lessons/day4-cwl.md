# Day4 CWL Exercise

[Slides](../slides/day4/day4.md)

## CWL environment setup
### Setup miniconda, [refer to day2 lesson](https://github.com/samesense/bfx-lessons-2019/blob/master/lessons/day2.md#setup-miniconda)

### Install CWL environment
```
$ conda create -y --name cwl-env python=3.6
$ source activate cwl-env
$ pip install cwlref-runner sevenbridges-python
```

### Install Rabix Composer
- http://rabix.io/
- https://github.com/rabix/cottontail-frontend


## Task 1 - Compose "_Hello World_" tool with code editor (15min)
[1st-tool.cwl](../slides/day4/examples/1st-tool.cwl)
```
cwlVersion: v1.0
class: CommandLineTool
baseCommand: echo
inputs:
  message:
    type: string
    inputBinding:
      position: 1
outputs: []
```
[1st-job.yml](../slides/day4/examples/1st-job.yml)
```
message: Hello world!
```
"Hello World" run
```bash
$(cwl-env) cwltool 1st-tool.cwl 1st-job.yml
/Users/zhuy/miniconda2/envs/cwl-env-3/bin/cwltool 1.0.20190228155703
Resolved '1st-tool.cwl' to 'file:///Users/zhuy/Documents/chopwork/git/bfx-lessons-2019/slides/day4/examples/1st-tool.cwl'
[job 1st-tool.cwl] /private/tmp/docker_tmpldca6q2h$ echo \
    'Hello world!'
Hello world!
Could not collect memory usage, job ended before monitoring began.
[job 1st-tool.cwl] completed success
{}
Final process status is success
```
Tips: CWL has syntax highlighting plugins for most editors, highly recommended:
- [vscode](https://github.com/manabuishii/vscode-cwl)
- [atom](https://github.com/manabuishii/language-cwl)
- [sublime](https://github.com/manabuishii/sublime-cwl-syntax)
- [vim](https://github.com/manabuishii/vim-cwl)
- [emacs](https://github.com/tom-tan/cwl-mode)
- [intellij](https://gitlab.com/AleksandrSl/cwl-plugin)
- [gedit](http://biosyntax.org/)

## Task 2 - Compose samtools view for S3 BAMs (15min)
Since v1.3, [htslib](http://www.htslib.org/download/) can access objects on Amazon S3, that allows [samtools](http://www.htslib.org/download/) to directly view BAM from S3 bucket. ([aws-cli](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) required)
```bash
$(cwl-env) export BAM=s3://1000genomes/phase1/data/NA12878/exome_alignment/NA12878.mapped.illumina.mosaik.CEU.exome.20110411.bam

$(cwl-env) samtools view $BAM | head | cut -f1-9
SRR098401.102126636	163	1	14921	22	71M1I4M	=	14958	112
SRR098401.102126636	83	1	14958	45	76M	=	14921	-112
SRR098401.51485842	163	1	16085	22	17M2D4M1D55M	=	16203	192
SRR098401.51485842	83	1	16203	40	9M1I66M	=	16085	-192
SRR098401.65849914	137	1	16439	7	76M	*	0	0
SRR098401.91675195	99	1	17392	45	76M	=	17456	134
SRR098401.100038301	163	1	17432	38	76M	=	17444	87
SRR098401.100038301	83	1	17444	24	76M	=	17432	-87
SRR098401.12552622	99	1	17446	38	76M	=	17512	141
SRR098401.91675195	147	1	17456	39	71M	=	17392	-134

$(cwl-env) samtools mpileup -r 20:100000-100010 $BAM
[mpileup] 1 samples in 1 input files
<mpileup> Set max per-file depth to 8000
20	100000	N	3	A$Aa	QBA
20	100001	N	2	Cc	DE
20	100002	N	2	Tt	ED
20	100003	N	2	Tt	DC
20	100004	N	2	Tt	DC
20	100005	N	2	Cc	EE
20	100006	N	2	Aa	CB
20	100007	N	2	Tt	BB
20	100008	N	2	Aa	AA
20	100009	N	2	Tt	AB
20	100010	N	2	Aa	BC
```

Task: compose a CWL by rabix composer to do `samtools view -H $BAM`

[example](../slides/day4/examples/samtools-s3bam-header.cwl) run
```bash
$(cwl-env) cwltool samtools-s3bam-header.cwl
usage: samtools-s3bam-header.cwl [-h] --bam BAM [job_order]
samtools-s3bam-header.cwl: error: the following arguments are required: --bam

$(cwl-env) cwltool samtools-s3bam-header.cwl --bam $BAM
Resolved 'samtools-s3bam-header.cwl' to 'file:///Users/zhuy/Documents/chopwork/git/bfx-lessons-2019/slides/day4/examples/samtools-s3bam-header.cwl'
[job samtools-s3bam-header.cwl] /private/tmp/docker_tmp8ig0uw_x$ docker \
    run \
    -i \
    --volume=/private/tmp/docker_tmp8ig0uw_x:/Kzllaw:rw \
    --volume=/private/tmp/docker_tmp48fhp5kh:/tmp:rw \
    --workdir=/Kzllaw \
    --read-only=true \
    --user=2049799698:1768498755 \
    --rm \
    --env=TMPDIR=/tmp \
    --env=HOME=/Kzllaw \
    --cidfile=/private/tmp/docker_tmp8z21b008/20190412054718-594425.cid \
    kfdrc/samtools:bootcamp \
    /bin/sh \
    -c \
    'samtools' 'view' -H s3://1000genomes/phase1/data/NA12878/exome_alignment/NA12878.mapped.illumina.mosaik.CEU.exome.20110411.bam > bam-header.txt
[job samtools-s3bam-header.cwl] Max memory used: 0MiB
[job samtools-s3bam-header.cwl] completed success
{
    "header": {
        "location": "file:///Users/zhuy/Documents/chopwork/git/bfx-lessons-2019/slides/day4/examples/bam-header.txt",
        "basename": "bam-header.txt",
        "class": "File",
        "checksum": "sha1$8d497d6ca70a0e1cf84f6b7480a3a0e31b75405b",
        "size": 5301,
        "path": "/Users/zhuy/Documents/chopwork/git/bfx-lessons-2019/slides/day4/examples/bam-header.txt"
    }
}
Final process status is success
```

[Slides to Cavatica](https://github.com/samesense/bfx-lessons-2019/blob/master/slides/day4/day4.md#cavatica)
