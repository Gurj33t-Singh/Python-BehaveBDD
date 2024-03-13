from resources import utils

def before_all(context):
    """
    gets env_config json file as dictionary
    """
    context.env_config=utils.get_json('env_config.json')

    context.host=context.env_config['Environment']['host']
    context.localhost=context.env_config['Environment']['localhost']
    context.state_code=context.env_config['Environment']['stateCode']
    context.city_code=context.env_config['Environment']['cityCode']

    """
    gets endpoints json file as dictionary
    """
    context.endpoints_json=utils.get_json('endpoints.json')