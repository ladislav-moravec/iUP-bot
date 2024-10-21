from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time

# Set up Firefox options (if needed)
firefox_options = Options()
firefox_options.add_argument("--start-maximized")  # Start with a maximized window

# Automatically download and set up the GeckoDriver using webdriver-manager
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options)

try:
    # Open the first webpage (login page)
    driver.get("https://www.iup.cz/registrace/")

    # Wait for the page to load (you can use explicit waits instead of sleep)
    time.sleep(2)

    # Fill in the email field
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys("moravec.ld@gmail.com")

    # Fill in the password field
    password_field = driver.find_element(By.ID, "heslo")
    password_field.send_keys("psIUP2121-")

    # Submit the form (click the button)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(),'Přihlásit se')]")
    submit_button.click()

    # Wait for the form submission to complete
    time.sleep(5)

    # Move to the new link
    driver.get("https://www.iup.cz/nasledne-vzdelavani/")

    # Wait for the new page to load
    time.sleep(2)

    # Click the link using the specified XPath
    target_link = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/p[4]/a")
    target_link.click()

    # Wait to see the result of the click action
    time.sleep(1900)

finally:
    # Close the browser
    driver.quit()
