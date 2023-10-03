from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    btn_success = (By.CSS_SELECTOR, "button.btn-success")
    input_country = (By.CSS_SELECTOR, "input[id='country']")
    suggestions = (By.CSS_SELECTOR, "div[class='suggestions'] ul li a")
    checkbox_primary = (By.CSS_SELECTOR, "div.checkbox-primary")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    success_message = (By.XPATH, "//strong[normalize-space()='Success!']")

    def buttonSuccess(self):
        return self.driver.find_element(*ConfirmPage.btn_success)

    def SelectCountry(self):
        return self.driver.find_element(*ConfirmPage.input_country)

    def suggestCountry(self):
        return self.driver.find_element(*ConfirmPage.suggestions)

    def selectCheckboxPrimary(self):
        return self.driver.find_element(*ConfirmPage.checkbox_primary)

    def SubmitForm(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def successMessage(self):
        return self.driver.find_element(*ConfirmPage.success_message)
