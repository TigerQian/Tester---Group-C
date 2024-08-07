*** Settings ***
Documentation   A test suite containing tests related to invalid login
Library  SeleniumLibrary
Suite Setup     Go to Website
Suite Teardown  Close Browser
Test Template   Invalid Login
Resource    resource.robot

*** Test Cases ***                       USERNAME        PASSWORD
T011 Invalid Email                       invalid         ${VALID_PASSWORD}
T012 Invalid Password                    ${VALID_Email}  invalid
T013 Invalid Email and Password          invalid         invalid

