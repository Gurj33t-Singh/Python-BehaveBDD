from typing import List, Optional
from dataclasses import dataclass

@dataclass
class Role:
    name: str
    code: str
    tenantId: str

@dataclass
class UserInfo:
    id: int
    uuid: str
    userName: str
    name: str
    mobileNumber: str
    emailId: str
    locale: Optional[str]
    type: str
    roles: List[Role]
    active: bool
    tenantId: str
    permanentCity: Optional[str]

@dataclass
class RequestInfo:
    apiId: str
    authToken: str
    userInfo: UserInfo

@dataclass
class Payload:
    RequestInfo: RequestInfo
    msgId: str

@dataclass
class PGR_search_params:
    tenantId: str
    serviceRequestId: str