from dataclasses import dataclass
from typing import List,Optional

@dataclass
class AuthPayload:
    username: str
    password: str
    grant_type: str
    scope: str
    tenantId: str
    userType: str

def generate_payload(
    USERNAME,
    PASSWORD,
    TENANTID,
    USERTYPE
):
    return AuthPayload(
        username=USERNAME,
        password=PASSWORD,
        grant_type='password',
        scope='read',
        tenantId=TENANTID,
        userType=USERTYPE
    )