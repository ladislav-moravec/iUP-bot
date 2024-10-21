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

    # Find the correct radio button's label and get its text
    correct_radio = driver.find_element(By.XPATH, "//input[@class='unspecified correct' and @value='2']")
    correct_label_text = driver.find_element(By.XPATH, f"//label[@for='{correct_radio.get_attribute('id')}']").text
    print(f"Correct answer text: {correct_label_text}")


    def click_ask_question_button(driver):
        try:
            # Find the "Položit otázku" button using its attributes
            ask_button = driver.find_element(By.XPATH,
                                             "//a[@class='btn btn-success btn-block spustitS' and @data-learn='0' and @data-id='55887']")

            # Click the button
            ask_button.click()
            print("Successfully clicked the 'Položit otázku' button.")
        except Exception as e:
            print(f"An error occurred while trying to click the button: {e}")


    click_ask_question_button(driver)

    # Find all labels for radio buttons
    all_labels = driver.find_elements(By.XPATH, "//label[starts-with(@for, 'Otazka')]")
    time.sleep(3)
    # Iterate over each label, compare its text, and if it matches the correct answer, click the label
    for label in all_labels:
        time.sleep(1)
        if label.text.strip() == correct_label_text.strip():
            # Click the label (since labels are clickable)
            label.click()
            print(f"Clicked radio button for: {label.text}")
            break

    # Wait for a short time before submitting
    time.sleep(2)

    # Find the "Vyhodnotit" button and click it
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit' and contains(text(),'Vyhodnotit')]")
    submit_button.click()

    # Wait to see the result of the action
    time.sleep(500)

finally:
    # Close the browser
    driver.quit()
