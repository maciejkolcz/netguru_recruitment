import chromedriver_binary
import sys
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome, ChromeOptions
from utils.utils import slow_typing


# This test is supposed to check if password strength check works
# when all fields are filled correctly


# open chrome
browser = Chrome()
browser.get('https://accounts.google.com/signup?hl=en')
time.sleep(2)

# if cookie notification pops up accept it so that it does not interfere
try:
    cookie_cta = browser.find_element_by_id('accept-cookie-notification')
    cookie_cta.click()
except NoSuchElementException:
    None

# define user input
userFirstName = "32"
userLastName = "48"
newUserName = "basehohen3248"
badPassword = "123456789"
badPasswordDict = {'shortMix': '!a34567', 'numbers': '12345678',
                   'numbersSymbols': '1234567!', 'symbols': '!@#$%^&*',
                   'letters': 'alamakota', 'username': 'basehohen3248',
                   'goodPassword': 'Alamak1!'}

# xpath to wrong password feedback
wrongPasswordFeedback = ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div" +
                         "/div/div[2]/div/div[1]/div/form/span/section/div/d" +
                         "iv/div[3]/div[2]/div[2]")

# put first name
firstNameField = browser.find_element_by_id("firstName")
slow_typing(firstNameField, userFirstName)
time.sleep(0.5)

# put last name
lastNameField = browser.find_element_by_id("lastName")
slow_typing(lastNameField, userLastName)
time.sleep(0.5)

# put user name
userNameField = browser.find_element_by_id("username")
slow_typing(userNameField, newUserName)
time.sleep(0.5)


# check if validation works, and password is wrong
def password_validation(badPasswordsDictionary):
    i = 0
    j = len(badPasswordsDictionary)
    for key in badPasswordsDictionary:
        try:
            # put bad password
            passwordField = browser.find_element_by_name("Passwd")
            slow_typing(passwordField, badPasswordsDictionary[key])
            # confirm bad password
            confirmField = browser.find_element_by_name("ConfirmPasswd")
            slow_typing(confirmField, badPasswordsDictionary[key])
            # click the next button
            nextButton = browser.find_element_by_id('accountDetailsNext')
            nextButton.click()
            time.sleep(1)
            # find feedback about wrong password
            browser.find_element_by_xpath(wrongPasswordFeedback)
            print(badPasswordsDictionary[key], "is not valid password. P" +
                                               "assword strength check works!")
            time.sleep(0.5)
            i += 1
            # empty password fields
            passwordField.clear()
            confirmField.clear()
            time.sleep(0.5)
        except NoSuchElementException:
            print(badPasswordsDictionary[key], "is valid password. Password " +
                                               "strength check failed!")
    return print(i, "out of", j, "proposed passwords are bad.")


password_validation(badPasswordDict)
