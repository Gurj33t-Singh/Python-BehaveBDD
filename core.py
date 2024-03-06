import requests
import json
from requests_toolbelt import MultipartEncoder

url='https://upyog-sandbox.niua.org'

def getJson(PATH):
 
    """ 
    Takes JSON file from PATH and converts on Dict obj
    args: PATH(str)
    returns: Dictionary Obj
    dependancy: import json """ 

    with open(PATH) as payload_file:
        return json.load(payload_file)

def callAPI(METHOD, API, URL=url, **kwargs):
    
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

def multiPartEnc(DICT):
    """ 
    Takes body dictionary and encodes as multipart obj
    args: DICT(Dictionary)
    returns: MultipartEncoder obj 
    dependacy: from requests_toolbelt import MultipartEncoder """

    return MultipartEncoder(fields=DICT)

def getResponseVal(RESPONSE, KEY):
    """ 
    Returns specific value for API response body
    args: RESPONSE(Response Obj), KEY(str)
    returns: value of provided key
    note: require raw response from requests module """
    return RESPONSE.json().get(KEY)

def update_value(dictionary_or_list, target_key, new_value):
    if isinstance(dictionary_or_list, dict):
        for key, value in dictionary_or_list.items():
            if isinstance(value, (dict, list)):
                update_value(value, target_key, new_value)
            elif key == target_key:
                dictionary_or_list[key] = new_value
    elif isinstance(dictionary_or_list, list):
        for item in dictionary_or_list:
            if isinstance(item, (dict)):
                update_value(item, target_key, new_value)
            else:
                dictionary_or_list.clear()
                dictionary_or_list.append(new_value)


method='post'
endpoint='/user/oauth/token'
json_body=getJson('requestPayload/mdms-v2/SchemaSearchv1.json')

# --------------Modify Payload---------------
constants_json=getJson('constants/mdms-v2.json')
keys=['codes', 'tenantId']


new_val=constants_json['payload']['codes']
update_value(dictionary_or_list=json_body, target_key=key, new_value=new_val)

print(json_body.get('SchemaDefCriteria'))

# print(type(modified_body))
# print(modified_body)
# --------------Modify Payload---------------


# encoded_body=multiPartEnc(json_body)
# req_headers={"Content-Type": encoded_body.content_type, "authorization": "Basic ZWdvdi11c2VyLWNsaWVudDo="}
# req_params={}

# raw_response=callAPI(METHOD=method, API=endpoint, Body=encoded_body, Headers=req_headers,Params=req_params)

# print('access_token: ', getResponseVal(RESPONSE=raw_response, KEY='access_token'))
# print('UserRequest', getResponseVal(RESPONSE=raw_response, KEY='UserRequest'))



# --------------MDMSv2 Params---------------
# method='post'
# endpoint='/mdms-v2/schema/v1/_search'
# json_body=json.dumps(getJsonPayload('mdms-v2/requestPayload/SchemaSearchv1.json'))
# req_headers={"Content-Type": "application/json"}
# req_params={}
# --------------MDMSv2 Req---------------
# raw_response=callAPI(METHOD=method, API=endpoint, Body=json_body, Headers=req_headers,Params=req_params)


# print('Request URL', raw_response.request.url)
# print('Request Header', raw_response.request.headers)
# print('Request Body', raw_response.request.body)

# print('\n\nResponse URL', raw_response.url)
# print('Response Header', raw_response.headers)
# print('Response Body', raw_response.json())
