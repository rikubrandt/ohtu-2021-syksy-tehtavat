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

Login After Successful Registration
    Register With Valid Username And Password
    Go To Login Page
    Set Username  uusikauttaja
    Set Password  tamasalis123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Register With Valid Username And Too Short Password
    Go To Login Page
    Set Username  oikeatama
    Set Password  lyh123
    Click Button  Login
    Page Should Contain  Invalid username or password


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

Register With Valid Username And Password
    Set Username  uusikauttaja
    Set Password  tamasalis123
    Set Password Confirmation  tamasalis123
    Submit Register
    Page Should Contain  Welcome to Ohtu Application!

Register With Valid Username And Too Short Password
    Set Username  oikeatama
    Set Password  lyh123
    Set Password Confirmation  lyh123
    Submit Register
    Register Should Fail With Message  Password must be 8 characters long and can't contain only characters.