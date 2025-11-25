from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")  # run without GUI
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://localhost:5000")
assert "Hello from Flask CI/CD!" in driver.page_source
print("Home page test passed!")

driver.quit()
