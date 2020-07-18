import json
import boto3
from chalice import Chalice, Response

s3 = boto3.client('s3')

app = Chalice(app_name='b2368-update-lambda')
app.debug = True

@app.route('/cpe_and_common/v2/Check.action', methods=['POST'], content_types=['text/json', 'application/json'])
def check_update():
    if app.debug:
        __debug_request()
    raw_req = app.current_request.raw_body
    json_req = app.current_request.json_body
    if not json_req:
        json_req = json.loads(raw_req)
    headers = app.current_request.headers
    if json_req['rules']['DeviceName'] == 'B2368':
        url = 'https://{}/api/FW'.format(headers['host'])
        return {'name': 'B2368', 'version': 'B2368_V100R001C00SPC085T', 'url': url, 'status': '0'}
    return {'status': '1'}

@app.route('/FW/full/filelist.xml', methods=['GET'])
def serve_file_list():
    if app.debug:
        __debug_request()
    xml = '<?xml version="1.0" encoding="utf-8"?>\n<root>\n<component>\n<name>FIRMWARE1</name>\n<compress>0</compress>\n</component>\n<files>\n<file>\n<spath>B2368_V100R001C00SPC085T.bin</spath>\n<dpath>B2368_V100R001C00SPC085T.bin</dpath>\n<operation>c</operation>\n<md5>97AFA38A6F57F6692A51B87B77EF665F</md5>\n<size>24248524</size>\n</file>\n</files>\n</root>\n'
    return Response(xml, headers={'Content-Type': 'text/xml'})

@app.route('/FW/full/B2368_V100R001C00SPC085T.bin', methods=['GET'])
def serve_firmware():
    if app.debug:
        __debug_request()
    _ = s3.get_object(Bucket='b2368-update-bypass-fw', Key='B2368_V100R001C00SPC085T.bin')
    url = s3.generate_presigned_url('get_object', Params={'Bucket': 'b2368-update-bypass-fw', 'Key': 'B2368_V100R001C00SPC085T.bin'}, ExpiresIn=120)
    return Response(None, status_code=302, headers={'Location': url})

def __debug_request():
    print('== DEBUG ==\n{}\n== DEBUG =='.format(json.dumps(app.current_request.to_dict())))
