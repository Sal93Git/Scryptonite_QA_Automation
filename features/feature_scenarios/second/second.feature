Feature: Testing the incrementor
    Scenario: Testing the increasing a number
        Given a new incrementor of size 5
        When we increment 10
        Then we should see 15

    Scenario: Test Decrease a number
        Given a new incrementor of size -2
        When we increment 20
        Then we should see 18

    Scenario: Test Decrease a number
        Given a new incrementor of size 0
        When we increment 15
        Then we should see 15
        Then web test