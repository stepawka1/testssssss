*** Settings ***
Library    ../project/Test.py


*** Variables ***
${angel_h}                90
${angel_v}                45
*** Test Cases ***
Test
    ${var}  Test   45  90   2   4
    Should Be True    ${var}
Test2
    ${var}  Test   49  64   0   4
    Should Be True    ${var}


*** Keywords ***
