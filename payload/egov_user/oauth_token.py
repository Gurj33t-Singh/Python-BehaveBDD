"""egov-user request dataclass"""
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

def generate_payload(username,
                    password,
                    tenantid,
                    user_type
                    ):
    return AuthPayload(username=username,
                        password=password,
                        grant_type='password',
                        scope='read',
                        tenantId=tenantid,
                        userType=user_type
                    )
