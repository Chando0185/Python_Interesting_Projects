from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import random


def human_typing(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(random.uniform(0.1, 0.3))


def startBot(username, password, url):
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    driver.get(url)
    driver.maximize_window()

    # Wait like a human after page load
    time.sleep(random.uniform(2, 4))

    # Find username field
    username_box = driver.find_element(By.NAME, "username")
    time.sleep(random.uniform(0.5, 1))
    human_typing(username_box, username)

    # Small pause
    time.sleep(random.uniform(1, 2))

    # Find password field
    password_box = driver.find_element(By.NAME, "password")
    human_typing(password_box, password)

    # Pause before clicking login
    time.sleep(random.uniform(1.5, 3))

    # Slight scroll (human behavior)
    driver.execute_script("window.scrollBy(0, 100);")
    time.sleep(random.uniform(0.5, 1))

    # Click login button
    login_btn = driver.find_element(By.ID, "login-btn")
    login_btn.click()

    # Stay on page to observe result
    time.sleep(15)
    driver.quit()


# -------- DRIVER CODE --------
username = "admin"
password = "123456"
url = "http://127.0.0.1:5000/login"

startBot(username, password, url)
