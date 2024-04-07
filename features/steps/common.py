"""
methods common among all modules
"""
import requests_toolbelt
from resources import utils
from resources.req_utils import RequestBuilder
from payload.egov_user import oauth_token

@given(u'Read constants from "{file_path}"')
def step_impl(context,file_path):
    context.constants=utils.get_json(file_path)

@given(u'Read endpoints of "{key}"')
def step_impl(context, key):
    """
    gets module specific API dictionary from endpoints_json file
    """
    context.endpoints=context.endpoints_json[key]

@given(u'Prepare request headers with "{key}" constants')
def step_impl(context, key):
     # Prepared headers
    context.headers=context.constants[key]

@given(u'Prepare request params with "{key}" constants')
def step_impl(context, key):
    # Prepared params
    context.params=context.constants[key]

@given(u'Login with "{key}" credentials')
def step_impl(context, key):
    # Prepared body with dataclass
    body=oauth_token.AuthPayload(
                                        username=context.env_config[key]['username'],
                                        password=context.env_config[key]['password'],
                                        userType=context.env_config[key]['type'],
                                        tenantId=context.state_code + '.' + context.city_code
                                    ).__dict__ # converted to dictionary

    # Converted body to multipart
    body=utils.multipart_encode(body)

    api=context.endpoints_json['authToken']['oauth']
    headers=context.auth_header
    headers['content-type']=body.content_type

    reqSpec=RequestBuilder()

    response=reqSpec.call_api(method='post', url=context.host,
                                            api=api, headers=headers, 
                                            params={}, data=body)
    
    context.access_token=response.json()['access_token']
    context.UserRequest=response.json()['UserRequest']
    # print(context.access_token, type(context.access_token))
    # print(context.UserRequest, type(context.UserRequest))

@when('Execute "{method}" request for "{api_key}" api with multipart body')
def step_impl(context, method, api_key):
    
    # if headers is not set, then use blank dict
    if not hasattr(context, 'headers'):
        context.headers={}

    # if params is not set, then use blank dict
    if not hasattr(context, 'params'):
        context.params={}
    
    # if body is multipart encoded, then set content-type header
    if isinstance(context.body, requests_toolbelt.MultipartEncoder):        
        context.headers['content-type']=context.body.content_type

    # get specific api from endpoints of current module 
    context.api=context.endpoints[api_key]
    
    # Create a RequestBuilder object to assign headers and params 
    context.req=RequestBuilder()
    context.req.set_headers(context.headers)
    context.req.set_params(context.params)

    context.response=context.req.call_api(method=method, url=context.host,
                                            api=context.api, headers=context.req.headers,
                                            params=context.req.params, data=context.body)

@when('Execute "{method}" request for "{api_key}" api with json body')
def step_impl(context, method, api_key):
    
    # if headers is not set, then use blank dict
    if not hasattr(context, 'headers'):
        context.headers={}

    # if params is not set, then use blank dict
    if not hasattr(context, 'params'):
        context.params={}
    
    # if body is multipart encoded, then set content-type header
    if isinstance(context.body, requests_toolbelt.MultipartEncoder):        
        context.headers['content-type']=context.body.content_type

    # get specific api from endpoints of current module 
    context.api=context.endpoints[api_key]
    
    # Create a RequestBuilder object to assign headers and params 
    context.req=RequestBuilder()
    context.req.set_headers(context.headers)
    context.req.set_params(context.params)

    context.response=context.req.call_api(method=method, url=context.host,
                                            api=context.api, headers=context.req.headers,
                                            params=context.req.params, json=context.body)
