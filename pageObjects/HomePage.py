from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop = (By.LINK_TEXT, "Shop")

    name = (By.CSS_SELECTOR, "div[class='form-group'] input[name='name']")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.CSS_SELECTOR, "input[id='exampleInputPassword1']")
    check = (By.CSS_SELECTOR, "input[id='exampleCheck1']")
    gender = (By.CSS_SELECTOR, "select[id='exampleFormControlSelect1']")
    status = (By.CSS_SELECTOR, "input[id='inlineRadio1']")
    submit_form = (By.XPATH, "(//input[@value='Submit'])[1]")
    message = (By.CSS_SELECTOR, "div.alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        check_out_page = CheckOutPage(self.driver)
        return check_out_page

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.password)

    def selectCheck(self):
        return self.driver.find_element(*HomePage.check)

    def selectGender(self):
        return self.driver.find_element(*HomePage.gender)

    def selectStatus(self):
        return self.driver.find_element(*HomePage.status)

    def selectSubmit(self):
        return self.driver.find_element(*HomePage.submit_form)

    def reviewMessage(self):
        return self.driver.find_element(*HomePage.message)
