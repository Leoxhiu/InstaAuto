from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# URL to scrape
url = "https://hypeauditor.com/top-instagram/"

# Navigate to the URL
driver.get(url)

# Initialize an empty list to store usernames
users = []

# Function to scrape usernames from current page
def scrape_usernames():
    # Find all elements with class 'contributor__name-content'
    name_elements = driver.find_elements(By.CLASS_NAME, 'contributor__name-content')
    
    # Extract usernames from elements and store in the list
    for element in name_elements:
        user = element.text
        users.append(user)

# Initial scraping for the first page
scrape_usernames()

# Close the WebDriver session
driver.quit()

# Print all scraped usernames
print(users)

# Open the file in write mode ('w' mode)
with open('users.txt', 'w') as file:
    # Write each user's name to the file followed by a newline
    for user in users:
        file.write(user + "\n")