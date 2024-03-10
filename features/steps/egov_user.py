"""
egov-user feature
"""
from resources import utils
from payload.egov_user import oauth_token

@given('Create login payload with "{key}" credentials')
def step_impl(context, key):
    """
    Prepares egov-user oauth payload with constants value
    """
    # Prepared body with dataclass
    context.body=oauth_token.AuthPayload(
        username=context.env_config[key]['username'],
        password=context.env_config[key]['password'],
        userType=context.env_config[key]['type'],
        grant_type='password',
        scope='read',
        tenantId=context.state_code + '.' + context.city_code
    ).__dict__ # converted to dictionary

    # Converted body to multipart
    context.body=utils.multipart_encode(context.body)
