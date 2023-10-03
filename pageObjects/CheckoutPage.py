from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    products = (By.CSS_SELECTOR, "h4:nth-child(1)")
    button_checkout = (By.CSS_SELECTOR, "a.btn-primary")

    def getProductTitle(self):
        return self.driver.find_elements(*CheckOutPage.products)

    def clickButtonCheckOut(self):
        self.driver.find_element(*CheckOutPage.button_checkout).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
