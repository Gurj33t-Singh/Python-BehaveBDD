from resources.utils import *
from resources.reqUtils import RequestBuilder


@given(u'Request object is ready')
def step_impl(context):
    context.req=RequestBuilder()

@given('Read constants "{constants_path}"')
def step_impl(context, constants_path):
    """
    gets constants json file as dictionary
    """
    context.constants_dict=getJson(constants_path)

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
    context.response=context.req.callAPI(METHOD=method, URL=context.req.url, API=endpoint, headers=context.req_header, params=context.req_param, data=context.payload_string)

@when('Execute "{method}" request for "{endpoint}" wiht multipart payload')
def step_impl(context, method, endpoint):
    # Added multipart header
    context.req_header['content-type']=context.multipart_body.content_type
    context.response=context.req.callAPI(METHOD=method, URL=context.req.url, API=endpoint, headers=context.req_header, params=context.req_param, data=context.multipart_body)

@then('Response code "{resCode:d}"')
def step_impl(context, resCode):
    assert context.response.status_code==resCode