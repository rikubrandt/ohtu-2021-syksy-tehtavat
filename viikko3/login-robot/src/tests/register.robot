*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input New Command And Create User
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command And Create User
    Input New Command And Create User
    Output Should Contain  User with username riku already exists


Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  dd  password
    Output Should Contain  Username has to be atleast 3 characters long.

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  username  pass
    Output Should Contain  Password has to be 8 characters long and can't only include letters and numbers 

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  username  password
    Output Should Contain  Password has to be 8 characters long and can't only include letters and numbers

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  riku  rikuriku123