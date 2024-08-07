*** Settings ***
Documentation   A test suite with a single test for valid login
Library  SeleniumLibrary
Suite Setup     Go to Website
Suite Teardown  Close Browser
Resource    resource.robot

*** Test Cases ***
T001 Valid Login
    [Documentation]     Valid user name and password to login
    Valid Login  ${VALID_Email}  ${VALID_PASSWORD}

