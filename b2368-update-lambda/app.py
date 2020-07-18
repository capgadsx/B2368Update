import json
from chalice import Chalice

app = Chalice(app_name='b2368-update-lambda')
app.debug = True

@app.route('/cpe_and_common/v2/Check.action', methods=['POST'])
def check_update():
    if app.debug:
        __debug_request()
    return {'status': '1'}

@app.route('/FW/full/filelist.xml', methods=['GET'])
def serve_file_list():
    if app.debug:
        __debug_request()

@app.route('/FW/full/B2368_V100R001C00SPC085T.bin', methods=['GET'])
def serve_firmware():
    if app.debug:
        __debug_request()

def __debug_request():
    print(' == DEBUG ==')
    print(json.dumps(app.current_request.to_dict(), indent='\t'))
    print(' == DEBUG ==')
