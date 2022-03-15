*** Settings ***
Resource  resource.robot
Test Setup  Input New Command and Create User

*** Test Cases ***
Register With Valid Username And Password
	Input Credentials  henkka  henkka123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username is in use

Register With Too Short Username And Valid Password
    Input Credentials  ka  kalle123
    Output Should Contain  Username should be at least 3 characters

Register With Valid Username And Too Short Password
    Input Credentials  henkka  henkka1
    Output Should Contain  Password should be at least 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  henkka  henkkahenkka
    Output Should Contain  Password should not consist solely of characters

*** Keywords ***
Input New Command And Create User
	Create User  kalle  kalle123
	Input New Command
