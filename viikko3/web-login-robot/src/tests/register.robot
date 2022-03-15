*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
	Set Username  henkka
	Set Password  henkka123
	Set Passwordconf  henkka123
	Submit Credentials
	Register Should Succeed

Register With Too Short Username And Valid Password
	Set Username  he
	Set Password  henkka123
	Set Passwordconf  henkka123
	Submit Credentials
	Register Should Fail With Message  Username should be at least 3 characters

Register With Valid Username And Too Short Password
	Set Username  henkka
	Set Password  henkka1
	Set Passwordconf  henkka1
	Submit Credentials
	Register Should Fail With Message  Password should be at least 8 characters

Register With Nonmatching Password And Password Confirmation
	Set Username  henkka
	Set Password  henkka123
	Set Passwordconf  henkka1234
	Submit Credentials
	Register Should Fail With Message  Passwords don't match!

Login After Successful Registration
	Set Username  henkka
	Set Password  henkka123
	Set Passwordconf  henkka123
	Submit Credentials
	Register Should Succeed
	Go To Login Page
	Set Username  henkka
    Set Password  henkka123
    Submit Credentialsold
    Login Should Succeed

Login After Failed Registration
	Set Username  he
	Set Password  henkka123
	Set Passwordconf  henkka123
	Submit Credentials
	Register Should Fail With Message  Username should be at least 3 characters
	Go To Login Page
	Set Username  he
    Set Password  henkka123
    Submit Credentialsold
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentialsold
	Click Button  Login

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Passwordconf
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
