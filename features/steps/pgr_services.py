from payload.pgr_services import search, create
import json

# PGR Search payload
@given(u'Prepare valid PGR "{reqType}" payload')
def step_impl(context, reqType):
    
    if reqType == 'search':
        context.reqInfo=search.RequestInfo(
                                    apiId='Rainmaker',
                                    authToken=context.access_token,
                                    userInfo=context.UserRequest
                                ).__dict__
        context.body=search.Payload(
                                RequestInfo=context.reqInfo, 
                                msgId='1712500690933|en_IN'
                                ).__dict__
    
    elif reqType == 'create':
        context.roles=create.Roles(
                                name='Citizen', 
                                code='CITIZEN', 
                                tenantId=context.state_code + '.' + context.city_code).__dict__

        context.citizen=create.Citizen(
                                    name='Jason', 
                                    type='CITIZEN',
                                    mobileNumber='8080808000', 
                                    roles=[context.roles], 
                                    tenantId=context.state_code + '.' + context.city_code
                                    ).__dict__

        context.locality=create.Locality(
                                    code='JLC477',
                                    name='Gali No,. 2 To Gali No. 6'
                                    ).__dict__

        context.address=create.Address(
                                    landmark='TEST LNDMRK',
                                    city=context.city_code,
                                    district=context.city_code,
                                    region=context.city_code,
                                    pincode='',
                                    locality=context.locality,
                                    geoLocation={}
                                    ).__dict__

        context.service=create.Service(
                                    tenantId=context.state_code + '.' + context.city_code, 
                                    serviceCode='NonSweepingOfRoad', 
                                    description='TEST ADD_DETAILS', 
                                    source='web', 
                                    address=context.address, 
                                    citizen=context.citizen, 
                                    additionalDetail={}
                                    ).__dict__

        context.reqInfo=create.RequestInfo(
                                    apiId='Rainmaker',
                                    authToken=context.access_token,
                                    userInfo=context.UserRequest,
                                    msgId='1712557009240|en_IN'
                                ).__dict__

        context.body=create.Payload(
                                RequestInfo=context.reqInfo, 
                                service=context.service,
                                workflow={'action': 'APPLY'},
                                ).__dict__

@given(u'Prepare valid PGR search params "{tenantId}" and "{serviceCode}"')
def step_impl(context, tenantId, serviceCode):
    context.params=search.PGR_search_params(
                                        tenantId=tenantId,
                                        serviceRequestId=serviceCode
                                    ).__dict__
    # print(type(context.params), context.params)

# PGR Create payload
@given(u'Prepare valid PGR create params "{tenantId}"')
def step_impl(context, tenantId):
    context.params=create.PGR_create_params(
                                        tenantId=tenantId
                                    ).__dict__
    # print(type(context.params), context.params)
