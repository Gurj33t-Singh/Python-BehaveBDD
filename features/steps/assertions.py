

@then('Response code is "{resCode:d}"')
def step_impl(context, resCode):
    print('Actual ResponseCode:', context.response.status_code)
    print('Actual Response:', context.response.json())
    print('Actual REQUEST:', context.response.request.url, context.response.request.body, context.response.request.headers)
    assert context.response.status_code==resCode

@then('Response message does not contain "{resMessage}"')
def step_impl(context, resMessage):
    res=context.response.json()
    assert resMessage not in res

@then('Response message contain "{resMessage}"')
def step_impl(context, resMessage):
    res=context.response.json()
    assert resMessage in res

@then('Validate response error code and message with "{key}" from constants')
def step_impl(context, key):
    
    error_code=context.constants['errors']['error_codes'][key]
    error_message=context.constants['errors']['error_messages'][key]
    res=context.response.json()

    print('Actual Response:', res)
    # print('Expected Response:', error_code, ': ', error_message)
    assert res['error']==error_code
    assert res['error_description']==error_message