from selenium.webdriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException
import sys
from utils.utils import slow_typing
import chromedriver_binary
import time


# This test is supposed to check if password strength check works
# when all fields are filled correctly and password consist of numbers only


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
userFirstName = "21"
userLastName = "37"
newUserName = "basehohen2137"
badPassword = "123456789"

# xpath to wrong password feedback
wrongPasswordFeedback = ("/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div" +
                         "/div/div[2]/div/div[1]/div/form/span/section/div/d" +
                         "iv/div[3]/div[2]/div[2]")

# put first name
firstNameField = browser.find_element_by_id("firstName")
slow_typing(firstNameField, userFirstName)
time.sleep(1)

# put last name
lastNameField = browser.find_element_by_id("lastName")
slow_typing(lastNameField, userLastName)
time.sleep(1)

# put user name
userNameField = browser.find_element_by_id("username")
slow_typing(userNameField, newUserName)
time.sleep(1)

# put bad password
passwordField = browser.find_element_by_name("Passwd")
slow_typing(passwordField, badPassword)
time.sleep(1)

# confirm bad password
confirmField = browser.find_element_by_name("ConfirmPasswd")
slow_typing(confirmField, badPassword)
time.sleep(1)

# click the next button
nextButton = browser.find_element_by_id('accountDetailsNext')
nextButton.click()
time.sleep(5)


# check if validation works, and password is wrong
def password_validation():
    try:
        browser.find_element_by_xpath(wrongPasswordFeedback)
        print("Password strength check works!")
    except NoSuchElementException:
        print("Password strength check failed!")


password_validation()
