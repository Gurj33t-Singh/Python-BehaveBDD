import requests
import json


def getJsonPayload(PATH):
 
    """ Params: Json file path
    Return JSON file as Dictionary """ 

    with open(PATH) as payload_file:
        return json.load(payload_file)


def callAPI(METHOD, URL, API, **kwargs):
    
    """ 
    METHOD: post, get
    optional args: 'Headers', 'Params', 'Body' as dictionary
    Returns Raw Response file 
    """

    if METHOD=='post':
        raw_response=requests.post(url=URL+API,
                                    headers=kwargs['Headers'],
                                    params=kwargs['Params'],
                                    json=kwargs['Body'])

    if METHOD=='get':
        raw_response=requests.get(url=URL+API,
                                    headers=kwargs['Headers'],
                                    params=kwargs['Params'])
    
    return raw_response


url='https://upyog-sandbox.niua.org'
endpoint='/mdms-v2/schema/v1/_search'
req_headers={"Content-Type": "application/json"}
req_params={}
json_body=getJsonPayload('mdms-v2/requestPayload/SchemaSearchv1.json')


raw_response=callAPI(METHOD='post',
                        URL=url, 
                        API=endpoint, 
                        Body=json_body, 
                        Headers=req_headers,
                        Params=req_params)


print('Request URL', raw_response.request.url)
print('Request Header', raw_response.request.headers)
print('Request Body', raw_response.request.body)

print('\n\nResponse URL', raw_response.url)
print('Response Header', raw_response.headers)
print('Response Body', raw_response.json())
