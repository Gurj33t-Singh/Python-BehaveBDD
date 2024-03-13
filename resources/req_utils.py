"""
RequestBuilder to handle dynamic json payload
"""
import requests

from resources import utils


class RequestBuilder:
    """
    RequestBuilder DocString
    """

    env_config=utils.get_json('env_config.json')['Environment']
    url: str
    body: dict
    headers: dict
    params: dict

    def __init__(self):
        self.url=self.env_config.get('host')
        self.headers={}
        self.params={}

    def set_body(self, **kwargs):
        """
        gets json file from path
        stores json as dict obj
        """
        if kwargs['json_path'] in kwargs:
            self.body=utils.get_json(kwargs['json_path'])
        elif kwargs['dataclass_obj'] in kwargs:
            self.body=kwargs['dataclass_obj'].__dict__
        elif kwargs['multipart_obj'] in kwargs:
            self.body=kwargs['multipart_obj']


    def set_body_dataclass(self, dataclass_obj):
        """
        dataclass obj body setter
        converts dataclass obj to dictionary
        """
        self.body=dataclass_obj.__dict__

    def set_body_multipart(self, obj):
        """multipart body setter"""
        self.body=obj

    def set_headers(self, headers: dict):
        """headers setter"""
        self.headers=headers

    def set_params(self, params: dict):
        """params setter"""
        self.params=params

    def call_api(self, method, url, api, **kwargs):
        """ 
        Calls api and gets raw response.
        Args: 
            method (str): post/get
            api (str): api endpoint
            url (str): Base url
        Optional Args:
            headers (dict): Headers
            params (dict): Query parameters
            data (json str): Request body (json.dumps())
        Returns:
            raw_response (requests obj): Raw response
        """
        if method=='post':
            raw_response=requests.post(url=url+api,
                                        headers=kwargs['headers'],
                                        params=kwargs['params'],
                                        data=kwargs['data'],
                                        timeout=10)

        if method=='get':
            raw_response=requests.get(url=url+api,
                                        headers=kwargs['Headers'],
                                        params=kwargs['Params'],
                                        timeout=10)
        
        return raw_response
