from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time

# Setup for Edge browser
options = Options()
options.add_argument("start-maximized")
service = Service(executable_path="msedgedriver.exe")  # Ensure it's in same folder or provide full path

driver = webdriver.Edge(service=service, options=options)

# Open login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Enter login details
driver.find_element(By.ID, "username").send_keys("student")
driver.find_element(By.ID, "password").send_keys("Password123")
driver.find_element(By.ID, "submit").click()

# Pause for 2 seconds
time.sleep(2)

# Validate login success
if "Logged In Successfully" in driver.page_source:
    print("✅ Test passed: Login successful.")
else:
    print("❌ Test failed: Login unsuccessful.")

# Close browser
driver.quit()
