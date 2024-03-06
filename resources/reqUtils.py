import requests
from resources.utils import *


class RequestBuilder:

    iniConf=getIniConfig('env.ini')
    url=''
    body={}
    headers={}
    params={}

    def __init__(self):
        print(self.iniConf.sections())
        self.URI=self.iniConf['API']['host']

    def add_payload(self, JSON_PATH):    
        self.body=getJson(JSON_PATH)

    def add_header(self, HEADERS):
        self.headers=HEADERS

    def add_params(self, PARAMS):
        self.params=PARAMS

    def callAPI(self, METHOD, API, URL, **kwargs):
        """ 
        Calls API and gets raw response.
        Args: 
            METHOD (str): post/get
            API (str): API endpoint
            URL (str): Base URL
        Optional Args:
            Headers (dict): Headers
            Params (dict): Query parameters
            Body (dict): Request body (json.dumps())
        Returns:
            raw_response (requests obj): Raw response
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
