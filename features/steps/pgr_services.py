from payload.pgr_services import search
import json


@given(u'Prepare valid PGR search payload')
def step_impl(context):

    context.reqInfo=search.RequestInfo(
                                apiId='Rainmaker',
                                authToken=context.access_token,
                                userInfo=context.UserRequest
                            )
    context.body=search.PGR_Search(
                            RequestInfo=context.reqInfo.__dict__, 
                            msgId='1712500690933|en_IN'
                            ).__dict__

@given(u'Prepare valid PGR search params')
def step_impl(context):
    context.params=search.PGR_Search_params(
                                        tenantId='pg.citya',
                                        serviceRequestId='PG-PGR-2024-04-02-001832'
                                    ).__dict__
    # print(type(context.params), context.params)
