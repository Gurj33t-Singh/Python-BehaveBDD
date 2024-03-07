from resources.reqUtils import RequestBuilder
from resources.utils import *
import json
from requestPayload.mdmsv2 import SchemaSearchv1



@given('Prepare login payload with "{constants_key}" constants')
def step_impl(context, constants_key):

    # Prepared body
    from requestPayload.egov_user import oauthToken
    context.dataclass_body=oauthToken.AuthPayload(
        username=context.constants_dict[constants_key]['username'],
        password=context.constants_dict[constants_key]['password'],
        tenantId=context.constants_dict[constants_key]['tenantId'],
        userType=context.constants_dict[constants_key]['userType'],
        grant_type='password',
        scope='read'
    )
    # Converted body to multipart 
    context.multipart_body=multiPartEnc(context.dataclass_body.__dict__)

    context.req_header={}
    context.req_param={}
