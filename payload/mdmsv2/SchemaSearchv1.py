from dataclasses import dataclass
from typing import List, Optional

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
    emailId: Optional[str]
    locale: Optional[str]
    type: str
    roles: List[Role]
    active: bool
    tenantId: str
    permanentCity: Optional[str]

@dataclass
class RequestInfo:
    apiId: str
    ver: Optional[str]
    ts: Optional[str]
    action: Optional[str]
    did: Optional[str]
    key: Optional[str]
    msgId: str
    authToken: str
    correlationId: Optional[str]
    userInfo: UserInfo

@dataclass
class SchemaDefCriteria:
    tenantId: str
    codes: List[str]

@dataclass
class SchemaSearch:
    RequestInfo: RequestInfo
    SchemaDefCriteria: SchemaDefCriteria