from selenium.webdriver import Chrome, ChromeOptions
from selenium.common.exceptions import NoSuchElementException
import chromedriver_binary
import time

# This test is supposed to check if user can create new acccount
# when username is duplicate value

#typing slowly as if it was human
def slow_typing(element, text):
   for character in text:
      element.send_keys(character)
      time.sleep(0.1)

#open chrome
browser = Chrome()
browser.get('https://accounts.google.com/signup?hl=en')
time.sleep(2)

# if cookie notification pops up accept it so that it does not interfere
try:
    cookie_cta = browser.find_element_by_id('accept-cookie-notification')
    cookie_cta.click()
except NoSuchElementException:
    None

duplicateUserName = "maciej.kolcz"
duplicateUserNameFeedback = "/html/body/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[2]/div[1]/div/div[2]/div[2]/div"

#put duplicate user name
userNameField = browser.find_element_by_id("username")
slow_typing(userNameField, duplicateUserName)
time.sleep(0.5)

#click the next button
nextButton = browser.find_element_by_id('accountDetailsNext')
nextButton.click()
time.sleep(5)

#check if validation works and duplicate name is not correct
try:
    browser.find_element_by_xpath(duplicateUserNameFeedback)
    print("Duplicate Username is not available!")
except NoSuchElementException:
    print("Duplicate Username check failed!")
