"""
egov-user feature
"""
from resources import utils
from Payload.egov_user import oauth_token

@given('Prepare login payload with "{constants_key}" constants')
def step_impl(context, constants_key):
    """
    Prepares egov-user oauth payload with constants value
    """
    # Prepared body with dataclass
    context.dataclass_body=oauth_token.AuthPayload(
        username=context.constants_dict[constants_key]['username'],
        password=context.constants_dict[constants_key]['password'],
        tenantId=context.constants_dict[constants_key]['tenantId'],
        userType=context.constants_dict[constants_key]['userType'],
        grant_type='password',
        scope='read'
    )

    # Converted body to multipart
    context.multipart_body=utils.multipart_encode(context.dataclass_body.__dict__)

    context.req_header={}
    context.req_param={}
