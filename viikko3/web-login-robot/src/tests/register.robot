*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  username
    Set Password  tama123je
    Set Password Confirmation  tama123je
    Submit Register
    Page Should Contain  Welcome to Ohtu Application!

Register With Too Short Username And Valid Password
    Set Username  jj
    Set Password  tama123je
    Set Password Confirmation  tama123je
    Submit Register
    Register Should Fail With Message  Username must be 3 characters long and contain only letters.

Register With Valid Username And Too Short Password
    Set Username  oikeatama
    Set Password  lyh123
    Set Password Confirmation  lyh123
    Submit Register
    Register Should Fail With Message  Password must be 8 characters long and can't contain only characters.

Register With Nonmatching Password And Password Confirmation
    Set Username  oikeatama
    Set Password  oikeasalasana123
    Set Password Confirmation  oikeasalasana321
    Submit Register
    Register Should Fail With Message  Password confirmation doesn't match.

*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${passcon}
    Input Password  password_confirmation  ${passcon}

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register
    Click Button  Register