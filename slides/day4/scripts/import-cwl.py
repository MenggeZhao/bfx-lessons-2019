import sevenbridges as sbg
import subprocess, json, os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-cwl", required=True)
parser.add_argument("-pjt", required=True)
parser.add_argument("-app", required=True)
args = parser.parse_args()

base_url = 'https://cavatica-api.sbgenomics.com/v2/'
token = os.environ['CAVATICA_ZYK_TOKEN']

api = sbg.Api(url=base_url, token=token)

cwl_str = subprocess.check_output(['rabix', '--resolve-app', args.cwl])
cwl_json = json.loads(cwl_str)
app_id = '/'.join((args.pjt, args.app))

try:
    app = api.apps.get(id=app_id)
    app_id = app_id + '/' + str(app.revision + 1)
except:
    pass

# install app
api.apps.install_app(app_id, cwl_json)
