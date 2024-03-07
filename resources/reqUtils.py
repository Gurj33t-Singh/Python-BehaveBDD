import requests
from resources.utils import *


class RequestBuilder:

    iniConf=getIniConfig('env.ini')
    url=''
    body={}
    headers={}
    params={}

    def __init__(self):
        self.url=self.iniConf['ENV']['host']

    def add_payload(self, JSON_PATH):    
        self.body=getJson(JSON_PATH)

    def add_payload_dataclass(self, dataClassObj):    
        self.body=dataClassObj.__dict__

    def add_payload_multipart(self, Obj):    
        self.body=Obj

    def add_header(self, HEADERS):
        """
        accepts headers dictionary file
        """
        self.headers=HEADERS

    def add_params(self, PARAMS):
        self.params=PARAMS

    def callAPI(self, METHOD, URL, API, **kwargs):
        """ 
        Calls API and gets raw response.
        Args: 
            METHOD (str): post/get
            API (str): API endpoint
            URL (str): Base URL
        Optional Args:
            headers (dict): Headers
            params (dict): Query parameters
            data (json str): Request body (json.dumps())
        Returns:
            raw_response (requests obj): Raw response
        """
        if METHOD=='post':
            raw_response=requests.post(url=URL+API,
                                        headers=kwargs['headers'],
                                        params=kwargs['params'],
                                        data=kwargs['data'])

        if METHOD=='get':
            raw_response=requests.get(url=URL+API,
                                        headers=kwargs['Headers'],
                                        params=kwargs['Params'])
        
        return raw_response
