class: CommandLineTool
cwlVersion: v1.0
requirements:
  - class: ShellCommandRequirement
  - class: DockerRequirement
    dockerPull: 'kfdrc/samtools:bootcamp'
  - class: InlineJavascriptRequirement
baseCommand: [samtools, view]
arguments:
  - position: 0
    shellQuote: false
    valueFrom: |-
      -H $(inputs.bam) > bam-header.txt
inputs:
  bam: string
outputs:
  header:
    type: File
    outputBinding:
      glob: 'bam-header.txt'
