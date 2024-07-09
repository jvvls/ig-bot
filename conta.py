from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from fake_useragent import UserAgent
from userGen import Usuario
import random
from vpn import VPN
import time

def random_delay():
    return random.uniform(0.2, 1.2)

ua = UserAgent()

# vpn = VPN()
# while VPN().ensure_connected(): pass

# brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
# chromedriver_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/chromedriver.exe"

# options = Options()
# options.binary_location = brave_path
# options.add_argument("--incognito")
# #options.add_argument(ua.random)
# # options.add_argument("--headless") # Uncomment to run in headless mode
# service = Service(executable_path=chromedriver_path)
# driver = webdriver.Chrome(service=service, options=options)

person = Usuario()
name = person.fullname()
user = person.user()
email = person.email()
password = person.password()

# try:
#     driver.get("https://www.instagram.com/accounts/emailsignup/")

#     WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.NAME, "emailOrPhone"))
#     )

#     email_or_phone = driver.find_element(By.NAME, "emailOrPhone")
#     full_name = driver.find_element(By.NAME, "fullName")
#     username = driver.find_element(By.NAME, "username")
#     password_field = driver.find_element(By.NAME, "password")

#     time.sleep(random_delay())
#     email_or_phone.send_keys(email)  # Replace with actual phone number

#     time.sleep(random_delay())
#     full_name.send_keys(name)

#     time.sleep(random_delay())
#     username.send_keys(user)

#     time.sleep(random_delay())
#     password_field.send_keys(password)

#     time.sleep(random_delay())
#     signup_button = driver.find_element(By.XPATH, "//button[@type='submit']")
#     signup_button.click()

#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//select[@title='Month:']"))
#     )

#     # Select birth date
#     select_month = Select(driver.find_element(By.XPATH, "//select[@title='Month:']"))
#     select_day = Select(driver.find_element(By.XPATH, "//select[@title='Day:']"))
#     select_year = Select(driver.find_element(By.XPATH, "//select[@title='Year:']"))

#     time.sleep(random_delay())
#     select_month.select_by_value("1")  # January

#     time.sleep(random_delay())
#     select_day.select_by_value("1")  # 1st

#     time.sleep(random_delay())
#     select_year.select_by_value("1990")  # 1990

#     time.sleep(random_delay())
#     next_button = driver.find_element(By.XPATH, "//button[@type='button' and text()='Next']")
#     next_button.click()

#     WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.NAME, "confirmationCode"))
#     )

#     # You would need to handle the verification code part here
#     time.sleep(120)

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     driver.quit()

with open("contas.txt", "a") as file:
    file.write(f"{name} : {email}, {user}, {password}.\n")
