from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(service=Service(), options=options)

    driver.get("http://example.com/login")

    # Fill out the login form
    driver.find_element(By.ID, "email_input").send_keys("test@example.com")
    driver.find_element(By.ID, "password_input").send_keys("password123")

    # Click the login button
    login_button = driver.find_element(By.ID, "loginButton")
    login_button.click()

    # Wait for the success message to appear
    try:
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "successMessage"))
        ).text
        assert success_message == "Welcome!", f"Login failed: {success_message}"
    except Exception as e:
        print("Error: ", e)
        driver.quit()
        return

    print("Login successful")
    driver.quit()


if __name__ == "__main__":
    test_login()
