from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Firefox options (if needed)
firefox_options = Options()
firefox_options.add_argument("--start-maximized")  # Start with a maximized window

# Specify the path to your geckodriver
gecko_driver_path = "/Users/ladislav/PycharmProjects/iUP-bot/utils/geckodriver"  # Update this path as necessary

# Create a Service object with the specified path
service = Service(executable_path=gecko_driver_path)

# Create the Firefox driver with the specified service and options
driver = webdriver.Firefox(service=service, options=firefox_options)

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

    # Click the link with the provided XPath
    target_link = driver.find_element(By.XPATH, "/html/body/div[1]/div[6]/div/div/p[4]/a")
    target_link.click()

    # Wait for the new page to load after the click
    time.sleep(3)

    # Click the 'Studovat oblast legislativy ČNB' button
    study_button = driver.find_element(By.XPATH, "//a[@class='spustitS' and @data-id='55887']")
    study_button.click()

    # Wait for the study page to load
    time.sleep(3)

    # Wait for the radio button to be present
    correct_radio = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='unspecified correct']"))
    )
    # Locate the text associated with the radio button
    correct_label = driver.find_element(By.XPATH, f"//label[@for='{correct_radio.get_attribute('id')}']")

    # Print the associated text for the correct answer
    print(f"Correct answer text: {correct_label.text}")

    # Optional: You can select the correct radio button if required
    # correct_radio.click()

    # Wait to see the result of the action
    time.sleep(1)

    # Use WebDriverWait to ensure the button is present
    question_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'spustitS') and text()='Položit otázku']"))
    )

    # Click the button
    question_button.click()
    time.sleep(1)

    ######## part to get correct answer from variable saved
    correct_label_text = "Hrubé nominální."  # Example value; replace with the actual text as needed

    # Use WebDriverWait to find all relevant labels
    labels = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//label[starts-with(@for, 'Otazka_')]"))
    )

    # Iterate through the labels to find the correct one and click it
    for label in labels:
        if label.text == correct_label_text:
            print(f"Found correct label: {label.text}")
            label.click()  # Click the label to select the associated radio button
            break  # Exit the loop after clicking the correct label
    ######## part to get correct answer from variable saved


finally:
    # Close the browser
    driver.quit()
