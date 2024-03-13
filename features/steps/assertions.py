

@then('Response code "{resCode:d}"')
def step_impl(context, resCode):
    assert context.response.status_code==resCode