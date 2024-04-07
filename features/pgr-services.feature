Feature: pgr-services service
    
    Background:
        Given Read constants from "constants/pgr-services.json"
        And Read endpoints of "pgr-services"

    @all @pgr
    Scenario Outline: PGR search API 
        Given Login with "<env_config key>" credentials
        And Prepare valid PGR search params
        And Prepare valid PGR search payload
        When Execute "post" request for "search" api with json body
        Then Response code is "200"
    Examples:
    |env_config key     |
    |Superuser            |