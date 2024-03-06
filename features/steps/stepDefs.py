from resources.reqUtils import RequestBuilder
from resources.utils import *
import json
from requestPayload.mdmsv2 import SchemaSearchv1


@given('Given "{username}", "{password}", "{tenantId}" and "{userType}"')
def step_impl(context, username, password, tenantId, userType):
    from requestPayload.egov_user import oauthToken
    context.payload=oauthToken.generate_payload(USERNAME=username, 
                                                PASSWORD=password, 
                                                TENANTID=tenantId, 
                                                USERTYPE=userType)
    context.dict_payload=context.payload.__dict__
    context.multipart_payload=multiPartEnc(context.dict_payload)
    context.req=RequestBuilder()
    print(context.req.url)


@given('"{key}" token is "{token}"')
def step_impl(context, key, token):
    context.req.add_header({key: token, 'content-type': context.multipart_payload.content_type})


@when('Execute "{method}" method for "{api}"')
def step_impl(context, method, api):
    print(context.req.url)
    context.response=context.req.callAPI(METHOD=method, URL=context.req.url, API=api, Headers=context.req.headers, Params={}, Body=context.multipart_payload)


@then('Response code "{resCode:d}"')
def step_impl(context, resCode):
    print(type(resCode), resCode, context.response.status_code, '\n', context.response.request.body, '\n', type(context.response.request.body))
    assert context.response.status_code==resCode