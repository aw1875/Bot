# Random Import
from random import shuffle, seed

# Faker Imports
from faker.providers.person.en import Provider
from faker import Faker

# Selenium Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Other Imports
import random
import os
import hashlib
import time

# Instantiate Faker
fake = Faker()

# Registration counter
registered = 0

# Start time
startTime = time.time()

# Creat list of fake names
first_names = list(set(Provider.first_names))
seed(4321)
shuffle(first_names)

# Start message
num = input("How many registrations would you like to complete: ")
print("Starting bot for " + num + " registrations...")

def fakeInfo():
    # Create fake information
    fn = first_names[i]
    un = fn + str(random.randint(1,999))
    emTemp = fake.email()
    emSplit = emTemp.split("@")
    em = un + "@" + emSplit[1]
    ps = str(random.randint(1,9999)) + fn + str(random.randint(1,999))
    return [fn, un, em, ps]

def main():
    # Open Browser
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options = chrome_options)
    driver.get("https://refer4.cash/wxlfy")

    # Click referral button
    button = driver.find_element_by_id('submit')
    button.click()

    # Wait
    driver.implicitly_wait(15)

    # Click sign up button
    button2 = driver.find_element_by_id('slider-1-slide-1-layer-26')
    button2.click()


    # Wait
    driver.implicitly_wait(5)

    # Get Elements
    name = driver.find_element_by_id('fullname')
    username = driver.find_element_by_id('username')
    email = driver.find_element_by_id('email')
    pass1 = driver.find_element_by_id('password')
    pass2 = driver.find_element_by_id('password_confirm')
    accept = driver.find_element_by_xpath('//*[@id="loginForm"]/div[7]/label/input');
    submit = driver.find_element_by_xpath('//*[@id="loginForm"]/button');

    # Create Fake Info
    person = fakeInfo()

    # Fill Elements
    name.send_keys(person[0])
    username.send_keys(person[1])
    email.send_keys(person[2])
    pass1.send_keys(person[3])
    pass2.send_keys(person[3])
    accept.click();

    # Wait
    time.sleep(2)

    # Submit page
    submit.click();

    # Wait
    time.sleep(5)
    driver.quit()

for i in range(int(num)):
    main()
    registered = registered + 1
    # print("Registrations so far: " + str(registered))
    if (i != (int(num) - 1)):
        waitTime = random.randint(30, 90)
        print("Waiting " + str(waitTime) + " seconds...")
        time.sleep(waitTime)

# Check runtime
endTime = time.time()
totalTime = endTime - startTime

# Print output message with results
print("Bot completed...")
if (totalTime < 60):
    if (registered > 1):
        print("Registered " + str(registered) + " accounts in " + str(int(totalTime)) + " seconds")
    else:
        print("Registered " + str(registered) + " account in " + str(int(totalTime)) + " seconds")
else:
    print("Registered " + str(registered) + " account in " + str(int(totalTime/60)) + " minutes and " + str(int(totalTime % 60)) + " seconds")
