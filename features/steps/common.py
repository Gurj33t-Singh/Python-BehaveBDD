"""
methods common among all modules
"""
import requests
import requests_toolbelt
from resources import utils
from resources.req_utils import RequestBuilder

@given(u'Read config "{file_path}"')
def step_impl(context, file_path):
    """
    gets json file as dictionary
    """
    context.env_config=utils.get_json(file_path)

    context.host=context.env_config['Environment']['host']
    context.localhost=context.env_config['Environment']['localhost']
    context.state_code=context.env_config['Environment']['stateCode']
    context.city_code=context.env_config['Environment']['cityCode']

@given(u'Read API "{file_path}"')
def step_impl(context, file_path):
    """
    gets json file as dictionary
    """
    context.api_config=utils.get_json(file_path)

@given(u'Read constants "{file_path}"')
def step_impl(context,file_path):
    context.constants=utils.get_json(file_path)

@given(u'Prepare request headers with "{key}" constants')
def step_impl(context, key):
     # Prepared headers
    context.headers=context.constants[key]

@given(u'Prepare request params with "{key}" constants')
def step_impl(context, key):
    # Prepared params
    context.params=context.constants[key]

@when('Execute "{method}" request for "{endpoint}"')
def step_impl(context, method, endpoint):
    
    context.req=RequestBuilder()

    if not hasattr(context, 'headers'):
        context.headers={}

    if not hasattr(context, 'params'):
        context.params={}
    
    if isinstance(context.body, requests_toolbelt.multipart.encoder.MultipartEncoder):        
        context.headers['content-type']=context.body.content_type
        
    context.req.set_headers(context.headers)
    context.req.set_params(context.params)
    context.response=context.req.call_api(method=method, url=context.host,
                                            api=endpoint, headers=context.req.headers,
                                            params=context.req.params, data=context.body)

@then('Response code "{resCode:d}"')
def step_impl(context, resCode):
    assert context.response.status_code==resCode
