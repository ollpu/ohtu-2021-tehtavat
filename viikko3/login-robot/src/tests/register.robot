*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Register User  abc  abcabca1
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  abc  abcabca1
    Register User  abc  cbacbac1
    Output Should Contain  Username already in use

Register With Too Short Username And Valid Password
    Register User  ab  abcabca1
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Register User  abc  abcabc1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Register User  abc  abcabca
    Output Should Contain  Password should not consist of only lowercase characters
