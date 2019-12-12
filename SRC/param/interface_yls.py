import os

from SRC.param.confighttp import ConfigHttp
from SRC.param import get_sign

#path=os.path.dirname(os.path.abspath('.'))+'\\script\\data\\http_config_yls.ini'
path='C:\\data\\http_config_yls.ini'
http=ConfigHttp(path)

def get_interface_data(url,request_param,method):
    param = {
        'appkey': http.get_appkey(),
        'token':  http.get_token()
    }
    if request_param != '':
        param.update(eval(request_param))
    else:
        param.update(request_param)
    param['usign'] = get_sign.uscgetApiUsign(param, http.get_secret())
    param['token'] = http.get_token()
    response = {}
    error=None
    if method == 'GET':
        response = http.get(url, param)
    else:
        response = http.post(url, param)
    if response['code'] == 200:
        if 'data' in response:
            error=response['data']
    else:
        error='999'

    return error

