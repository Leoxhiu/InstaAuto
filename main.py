from dotenv import load_dotenv
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Setup environment
load_dotenv()
USERNAME = os.getenv('INSTA_USERNAME')
PASSWORD = os.getenv('INSTA_PASSWORD')
TARGET_POST = os.getenv('TARGET_POST')
USER_PER_BATCH = int(os.getenv('USER_PER_BATCH'))
REST_AFTER_BATCH = int(os.getenv('REST_AFTER_BATCH'))

# Setup selenium driver
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Get users
with open('users.txt', 'r') as file:
    # Read all lines
    users = file.readlines()

# Strip newline characters and create a list
users = [user.strip() for user in users]
print(users)

# Access instagram
url='https://www.instagram.com/'
driver.get(url)

# Login
time.sleep(5)
username=driver.find_element(By.CSS_SELECTOR, "input[name='username']")
password=driver.find_element(By.CSS_SELECTOR, "input[name='password']")
username.clear()
password.clear()
username.send_keys(USERNAME)
password.send_keys(PASSWORD)
login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
login.click()

# "Not Now" for save login info
time.sleep(5)
notnow = driver.find_element(By.CSS_SELECTOR, "._a9--._ap36._a9_1")
notnow.click()

# Go to post
time.sleep(5)
post=TARGET_POST
driver.get(post)

# Locate share button
time.sleep(5)
share = driver.find_element(By.CLASS_NAME, "_abl-")
share.click()

# Locate search bar
time.sleep(5)
search_bar = driver.find_element(By.CSS_SELECTOR, "input[name='queryBox']")

count=0
total_steps=0
for user in users:
    time.sleep(2)
    search_bar.send_keys(user)

    # Find and click the first user
    try:
        # Wait for the first user to be clickable, adjust timeout as necessary
        time.sleep(10)
        first_user = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="x1n2onr6"]/span/img')))
        first_user.click()
        count+=1
        total_steps+=1

        print('count =' + str(count))
        print('total_steps =' + str(total_steps))

        # Send the post when hit target number of selected users
        if count==USER_PER_BATCH or total_steps == len(users):
            time.sleep(5)
            try:
                # Wait for the element to be clickable based on its text content
                send_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//div[contains(text(), "Send separately")]'))
                )
                
                # Click on the element
                send_button.click()
                
            except Exception as e:
                print(f"Error occurred: {e}")

            # Reset count and refresh webpage, rest for 15 minutes
            count=0
            rest_time = REST_AFTER_BATCH * 60
            time.sleep(rest_time)

            # Refresh page
            driver.refresh()

            # Locate share button again
            time.sleep(5)
            share = driver.find_element(By.CLASS_NAME, "_abl-")
            share.click()

            # Locate search bar again
            time.sleep(5)
            search_bar = driver.find_element(By.CSS_SELECTOR, "input[name='queryBox']")

            # If finish user list, terminate program
            if total_steps == len(users):
                time.sleep(30)
                driver.quit()

    except TimeoutException:
        print("User not found or clickable within 10 seconds")