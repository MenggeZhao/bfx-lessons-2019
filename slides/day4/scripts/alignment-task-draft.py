import sevenbridges as sbg
import argparse
import os, yaml

base_url = 'https://cavatica-api.sbgenomics.com/v2/'
token = os.environ['CAVATICA_ZYK_TOKEN']
api = sbg.Api(url=base_url, token=token)

parser = argparse.ArgumentParser()
parser.add_argument("-app", required=True)
parser.add_argument("-ref", required=True)
parser.add_argument("-pjt", required=True)
parser.add_argument("-name", required=True)
args = parser.parse_args()

# prepare input reference files
references = api.files.query(project='yuankun/kf-reference').all()
for each in references:
    # print each.size
    fq = api.files.query(project=args.pjt, names=[each.name])
    if fq.total == 0:
        # file not exist, copy over
        each.copy(project=args.pjt)
    else:
        fq = list(fq)[0]
        if each.size != fq.size:
            # file name same, size differ, overwrite
            fq.delete()
            each.copy(project=args.pjt)

# load input ref as json object
ref_input_yaml = args.ref
with open(ref_input_yaml, 'r') as y:
    ref_input = yaml.load(y)
for k in ref_input:
    if type(ref_input[k]) is str:
        f = api.files.query(project=args.pjt, names=[ref_input[k]])[0]
    if type(ref_input[k]) is list:
        f = []
        for i in ref_input[k]:
            f.append(api.files.query(project=args.pjt, names=[i])[0])
    ref_input[k] = f

# create task draft
api.tasks.create(
    name=args.name,
    project=args.pjt,
    app=args.app,
    inputs=ref_input)
