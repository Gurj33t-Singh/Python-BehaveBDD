Feature: egov-user service
    
    Background: 
        # read configs
        Given Read config "config.json"
        # And Read API ""
        And Read constants "constants/egov-user.json"

    @static
    Scenario: Verify Login API 
        Given Create login payload with "Citizen" credentials
        And Prepare request headers with "headers" constants
        When Execute "post" request for "/user/oauth/token"
        Then Response code "200"