import json
from flask import Flask, jsonify, request, Response, send_file

app = Flask(__name__)

@app.route('/cpe_and_common/v2/Check.action', methods=['POST'])
def do_update():
	drouter = json.loads(str(request.get_data(), 'utf-8'))
	print('Parsed request data from router:', drouter)
	if drouter['rules']['DeviceName'] == 'B2368':
		return jsonify({'name': 'B2368', 'version': 'B2368_V100R001C00SPC085T', 'url': 'http://fwup.duckdns.org/FW', 'status': '0'}) 
	return jsonify({'status': '1'}) 

@app.route('/FW/full/filelist.xml', methods=['GET'])
def serve_file_list():
	xml = '<?xml version="1.0" encoding="utf-8"?>\n<root>\n<component>\n<name>FIRMWARE1</name>\n<compress>0</compress>\n</component>\n<files>\n<file>\n<spath>B2368_V100R001C00SPC085T.bin</spath>\n<dpath>B2368_V100R001C00SPC085T.bin</dpath>\n<operation>c</operation>\n<md5>97AFA38A6F57F6692A51B87B77EF665F</md5>\n<size>24248524</size>\n</file>\n</files>\n</root>\n'
	return Response(xml, mimetype='text/xml')

@app.route('/FW/full/B2368_V100R001C00SPC085T.bin', methods=['GET'])
def serve_fw():
	print('Sending firmware file')
	return send_file('./B2368_V100R001C00SPC085T.bin')

if __name__ == '__main__':
	app.run()

# status=1 => NO UPDATE; status=0 => UPDATE
# http://fwup.duckdns.org/cpe_and_common/v2/Check.action?latest=true
# CPE and Module have new FW, it will update Module FW first.
# After Module update finished and device reboot, it will update CPE firmware automatically when device connects to Internet. The procedure will reboot device two times in total, please refresh your web page manually.
# Module Information:
# Current software version is 11.620.18.24.00.
# Server software version is
# CPE Information:
# Current software version is B2368_V100R001C00SPC114.
# Server software version is
# Upgrade now?Upgrade Status :

## "{"status":"1"}"
# Parsed request data: {'rules': {'DeviceName': 'B2368', 'C_version': 'C00', 'Firmware': 'B2368_V100R001C00SPC114', 'deviceId': 'S200Y02025269', 'udid': 'BBC16AD8FA0A9541F9B4D82E83A569FCAE174FFB46A4E3B6A168643D8B949D15'}}
# Parsed request data: {'rules': {'DeviceName': 'B2368-Modem', 'C_version': 'C00', 'Firmware': '11.620.18.24.00', 'deviceId': 'S200Y02025269', 'udid': 'BBC16AD8FA0A9541F9B4D82E83A569FCAE174FFB46A4E3B6A168643D8B949D15'}}
# https://conory.com/blog/73696
# <?xml version="1.0" encoding="utf-8"?>
# <root>
# <component>
# <name>FIRMWARE1</name>
# <compress>0</compress>
# </component>
# <files>
# <file>
# <spath>changelog.xml</spath>
# <dpath>changelog.xml</dpath>
# <operation>c</operation>
# <md5>8D63D0AC3C840166A70BD4655FA243DB</md5>
# <size>2239</size>
# </file>
# <file>
# <spath>E5885Ls-93a_UPDATE_21.182.63.00.148_WEBUI_21.100.37.00.148_NE5.ZIP</spath>
# <dpath>E5885Ls-93a_UPDATE_21.182.63.00.148_WEBUI_21.100.37.00.148_NE5.ZIP</dpath>
# <operation>c</operation>
# <md5>1A0D0E4376AE0A8CDEF63D9B28B6CB80</md5>
# <size>37430116</size>
# </file>
# </files>
# </root>


