import os

from SRC.param.confighttp import ConfigHttp
from SRC.param import get_sign

#path=os.path.dirname(os.path.abspath('.'))+'\\script\\data\\http_config.ini'
path='C:\\http_config.ini'
http=ConfigHttp(path)

def get_interface_data(url,request_param,method):
    param = {
        'appkey': http.get_appkey(),
        'secret': http.get_secret(),
        'token':  http.get_token()
    }
    if request_param != '':
        param.update(eval(request_param))
    else:
        param.update(request_param)
    param['sign'] = get_sign.udhgetApiUsign(param, http.get_secret())
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

