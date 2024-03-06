from resources.reqUtils import * 

r=RequestBuilder(METHOD='get', API='test')
r.add_header()
r.add_params()
r.add_payload()
r.callAPI()