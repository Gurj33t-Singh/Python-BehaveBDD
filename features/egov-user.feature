Feature: egov-user service
    
    Background:
        Given Read constants from "constants/egov-user.json"
        And Read endpoints of "authToken"

    @static
    Scenario: Verify Login API 
        Given Create login payload with "Citizen" credentials
        And Prepare request headers with "headers" constants
        When Execute "post" request for "oauth" api
        Then Response code "200"