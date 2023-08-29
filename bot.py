from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import sys

password = sys.argv[1]
make = sys.argv[2]
model = sys.argv[3]
licensePlt = sys.argv[4]
email = sys.argv[5]

driver = webdriver.Chrome()

def submit(elementId):
    button = driver.find_element(By.ID, elementId)
    button.click()
    time.sleep(3)

def inputText(elementId, text):
    input = driver.find_element(By.ID, elementId)
    input.send_keys(text)

def emailConfirmation():
    submit('email-confirmation')
    inputText('emailConfirmationEmailView', email)
    submit('email-confirmation-send-view')
    time.sleep(3)

driver.get('https://www.register2park.com/register')

propName = driver.find_element(By.ID, 'propertyName')
propName.send_keys('High View')

submit('confirmProperty')


propRadio = driver.find_element(By.NAME, 'property')
propRadio.click()

submit('confirmPropertySelection')

submit('registrationTypeVisitor')

inputText('guestCode', password)

submit('propertyGuestCode')

inputText('vehicleMake', make)
inputText('vehicleModel', model)
inputText('vehicleLicensePlate', licensePlt)
inputText('vehicleLicensePlateConfirm', licensePlt)

submit('vehicleInformationVIP')

circle = driver.find_element(By.CLASS_NAME, 'circle-inner')
message = circle.find_element(By.TAG_NAME, 'h2').text

if "Denied" in message: 
    print('DENIED Loser')
else:
    emailConfirmation()

driver.quit()