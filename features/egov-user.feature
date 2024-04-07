Feature: egov-user service
    
    Background:
        Given Read constants from "constants/egov-user.json"
        And Read endpoints of "authToken"

    @all
    Scenario Outline: Verify Login API 
        Given Create login payload with "<env_config key>" credentials
        And Prepare request headers with "headers" constants
        When Execute "post" request for "oauth" api with multipart body
        Then Response code is "200"
        Then Response message contain "access_token"
    Examples:
        |env_config key     |
        |Citizen            |
        |alternateCitizen   |
        |citizenArchitect   |
        |Superuser          |

    @all
    Scenario Outline: Verify Login API with invalid credentials
        Given Create login payload with invalid credentials "<username>", "<password>", "<userType>"
        And Prepare request headers with "headers" constants
        When Execute "post" request for "oauth" api with multipart body
        Then Response code is "400"
        Then Response message does not contain "access_token"
        Then Validate response error code and message with "invalidCredentials" from constants
    Examples: 
        |username     |password   |userType    |
        |PTSU         |eGov@111   |EMPLOYEE    |
        |8080808000   |111111     |CITIZEN     |
        |INPTSU       |eGov@123   |EMPLOYEE    |
        |8080808111   |123456     |CITIZEN     |

    @all
    Scenario Outline: Verify Login API with invalid userType
        Given Create login payload with invalid credentials "<username>", "<password>", "<userType>"
        And Prepare request headers with "headers" constants
        When Execute "post" request for "oauth" api with multipart body
        Then Response code is "400"
        Then Response message does not contain "access_token"
        Then Validate response error code and message with "invalidCredentials" from constants
    Examples: 
        |username     |password   |userType    |
        |8080808000   |123456     |EMPLOYEE    |
        |INPTSU       |eGov@123   |CITIZEN     |