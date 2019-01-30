from botocore.vendored import requests
import logging

#logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

CVAPI_BASEURL="https://cds-aws-bundles.netapp.com:8080/v1"
CVAPI_APIKEY = "enter your CVS API key"
CVAPI_SECRETKEY = "enter your CVS secret key"

#Headers
HEADERS = {
    'content-type': 'application/json',
    'api-key': CVAPI_APIKEY,
    'secret-key': CVAPI_SECRETKEY
    }

getfilesystemDetailsHeaders = {
    'content-type': 'application/json',
    'api-key': CVAPI_APIKEY,
    'secret-key': CVAPI_SECRETKEY
}


filesystemURL = CVAPI_BASEURL + "/FileSystems"
filesystemDetails = CVAPI_BASEURL + "/FileSystems" + "/c756d817-d46e-3d09-8080-790bec931401/MountTargets"
filesystemCreateURL = CVAPI_BASEURL

def lambda_handler(event, context):
    getResult = requests.get(url=filesystemURL, headers=HEADERS)
    print("get File system success, the response code : ", getResult.status_code)
    fileSystemsData = getResult.json()
    for i in fileSystemsData:
        fileSystemId = (i['fileSystemId'])
        name = (i['name'])
        print("FileSystemId : ", fileSystemId, " =   VolumeName : ", name)