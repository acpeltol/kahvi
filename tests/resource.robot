*** Settings ***
Library  SeleniumLibrary
Library  ../src/AppLibrary.py

*** Variables ***
${SERVER}       localhost:5001
${DELAY}        0.5 seconds
${ADD_REFERENCE_URL}  http://${SERVER}
${BROWSER}      chrome
${HEADLESS}     false

*** Keywords ***
Open And Configure Browser
    IF  $BROWSER == 'chrome'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].ChromeOptions()  sys
    ELSE IF  $BROWSER == 'firefox'
        ${options}  Evaluate  sys.modules['selenium.webdriver'].FirefoxOptions()  sys
    END
    IF  $HEADLESS == 'true'
        Set Selenium Speed  0
        Call Method  ${options}  add_argument  --headless
    ELSE
        Set Selenium Speed  ${DELAY}
    END
    Open Browser  browser=${BROWSER}  options=${options}

Add Reference Page Should Be Open
    Title Should Be  Latex viite sovellus

Go To Add Reference Page
    Go To  ${ADD_REFERENCE_URL}
