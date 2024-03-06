import requests
from resources.utils import *


class RequestBuilder:

    iniConf=utils.getIniConfig('DigitEnv.ini')
    url
    body
    headers
    params
    # encoded_body=multiPartEnc(json_body)
    # req_headers={"Content-Type": encoded_body.content_type, "authorization": "Basic ZWdvdi11c2VyLWNsaWVudDo="}

    def __init__(self):
        self.url=self.iniConf['ENV']['host']

    def add_payload(self, JSON_PATH):    
        self.body=getJson(JSON_PATH)

    def add_header(self, HEADERS):
        self.headers=HEADERS

    def add_params(self, PARAMS):
        self.params=PARAMS

    def callAPI(METHOD, API, URL=self.url, **kwargs):
        """ 
        calls API and gets raw response
        args: METHOD(str)post/get, API(str)
        optional args: URL(str), Headers(kwarg), Params(kwarg), Body(kwarg) <- (json.dumps())
        returns: raw_response(requests obj) 
        dependacy: import requests
        """
        if METHOD=='post':
            raw_response=requests.post(url=URL+API,
                                        headers=kwargs['Headers'],
                                        params=kwargs['Params'],
                                        data=kwargs['Body'])

        if METHOD=='get':
            raw_response=requests.get(url=URL+API,
                                        headers=kwargs['Headers'],
                                        params=kwargs['Params'])
        
        return raw_response

"""     def getResponseVal(self, RESPONSE, KEY):
        
        Returns specific value for API response body
        args: RESPONSE(Response Obj), KEY(str)
        returns: value of provided key
        note: require raw response from requests module
        return RESPONSE.json().get(KEY) """

