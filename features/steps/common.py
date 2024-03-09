"""
methods common among all modules
"""
from resources import utils
from resources.req_utils import RequestBuilder


@given(u'Request object is ready')
def step_impl(context):
    """
    create RequestBuilder object
    """
    context.req=RequestBuilder()

@given('Read constants "{constants_path}"')
def step_impl(context, constants_path):
    """
    gets constants json file as dictionary
    """
    context.constants_dict=utils.get_json(constants_path)

@given(u'Prepare request headers with "{constants_key}" constants')
def step_impl(context, constants_key):
     # Prepared headers
    context.req_header=context.constants_dict[constants_key]

@given(u'Prepare request params with "{constants_key}" constants')
def step_impl(context, constants_key):
    # Prepared params
    context.req_param=context.constants_dict[constants_key]

@when('Execute "{method}" request for "{endpoint}"')
def step_impl(context, method, endpoint):
    context.response=context.req.call_api(method=method, url=context.req.url,
                                        api=endpoint, headers=context.req_header,
                                        params=context.req_param, data=context.payload_string)

@when('Execute "{method}" request for "{endpoint}" wiht multipart payload')
def step_impl(context, method, endpoint):
    # Added multipart header
    context.req_header['content-type']=context.multipart_body.content_type
    context.response=context.req.call_api(method=method, url=context.req.url,
                                        api=endpoint, headers=context.req_header, 
                                        params=context.req_param, data=context.multipart_body)

@then('Response code "{resCode:d}"')
def step_impl(context, resCode):
    assert context.response.status_code==resCode
