Feature: Verify Add and Delete Book API 

    @static
    Scenario Outline: Verify Login API 
        Given Given <username> and <password> 
        And payload
        When Execute Post method for AddBook API
        Then Book is successfully is added

        Examples:
        |username   |password   |
        |MDMSAD2    |upyogTest@123|