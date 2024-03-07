data = {
    "headers": {
        "authorization": "Basic ZWdvdi11c2VyLWNsaWVudDo="
    },
    "credentials": {
        "username": "MDMSAD2",
        "password": "upyogTest@123",
        "tenantId": "pg",
        "userType": "EMPLOYEE"
    },
    "errors": {
        "error_codes": {
            "invalidCredentials": ""
        },
        "error_messages": {
            "invalidCredentials": ""
        }
    }
}

for k, v in data.items():
    globals()[k]=v


print(headers)