Feature: Verify Add and Delete Book API 

    @static
    Scenario Outline: Verify Login API 
        Given Given "<username>", "<password>", "<tenantId>" and "<userType>"
        And "authorization" token is "Basic ZWdvdi11c2VyLWNsaWVudDo="
        When Execute "post" method for "/user/oauth/token"
        Then Response code "200"

        Examples:
        |username   |password   |tenantId   |userType   |
        |MDMSAD2    |upyogTest@123|pg   |EMPLOYEE   |