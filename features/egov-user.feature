Feature: egov-user service
    
    Background: 
        Given Read constants "constants/egov-user.json"
        And Request object is ready

    @static
    Scenario: Verify Login API 
        Given Prepare login payload with "credentials" constants
        And Prepare request headers with "headers" constants
        When Execute "post" request for "/user/oauth/token" wiht multipart payload
        Then Response code "200"