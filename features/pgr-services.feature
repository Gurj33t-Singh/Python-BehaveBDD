Feature: pgr-services service
    
    Background:
        Given Read constants from "constants/pgr-services.json"
        And Read endpoints of "pgr-services"

    @all @pgr
    Scenario Outline: PGR search API 
        Given Login with "<env_config key>" credentials
        And Prepare valid PGR search params "<tenantId>" and "<serviceCode>"
        And Prepare valid PGR "search" payload
        When Execute "post" request for "search" api with json body
        Then Response code is "200"
    Examples:
    |env_config key   |tenantId |serviceCode             |
    |Superuser        |pg.citya |PG-PGR-2024-04-02-001832|

    @all @pgr
    Scenario Outline: PGR create API 
        Given Login with "<env_config key>" credentials
        And Prepare valid PGR create params "<tenantId>"
        And Prepare valid PGR "create" payload
        When Execute "post" request for "create" api with json body
        Then Response code is "200"
    Examples:
    |env_config key   |tenantId |
    |Superuser        |pg.citya |