from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class Locality:
    code: str
    name: str

@dataclass
class Roles:
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
    emailId: Any
    locale: Any
    type: str
    roles: List[Roles]
    active: bool
    tenantId: str
    permanentCity: Any

@dataclass
class Address:
    landmark: str
    city: str
    district: str
    region: str
    pincode: str
    locality: Locality
    geoLocation: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Citizen:
    name: str
    type: str
    mobileNumber: str
    roles: List[Roles]
    tenantId: str

@dataclass
class Service:
    tenantId: str
    serviceCode: str
    description: str
    source: str
    address: Address
    citizen: Citizen
    additionalDetail: Dict[str, Any] = field(default_factory=dict)

@dataclass
class UserInfo:
    id: int
    uuid: str
    userName: str
    name: str
    mobileNumber: str
    emailId: Any
    locale: Any
    type: str
    roles: List[Roles]
    active: bool
    tenantId: str
    permanentCity: Any

@dataclass
class RequestInfo:
    apiId: str
    authToken: str
    userInfo: UserInfo
    msgId: str
    plainAccessRequest: Dict[str, Any] = field(default_factory=dict)

@dataclass
class Workflow:
    action: str

@dataclass
class Payload:
    service: Service
    workflow: Workflow
    RequestInfo: RequestInfo

@dataclass
class PGR_create_params:
    tenantId: str