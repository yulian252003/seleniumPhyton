import time
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        self.driver.implicitly_wait(5)
        wait = WebDriverWait(self.driver, 10)  # Consider this element instead of Sleep
        product_name = "Blackberry"
        expected_message = "Success!"
        exited_list = ['iphone X', 'Samsung Note 8', 'Nokia Edge', 'Blackberry']

        check_out_page = homepage.shopItems()
        log.info("getting all the product titles")
        products = check_out_page.getProductTitle()
        for item in products:
            product = item.text
            log.info(product)
            if product == product_name:
                index_item = exited_list.index(product_name)
                locator = f"app-card:nth-child({index_item + 1}) > div:nth-child(1) > div:nth-child(3) > button"
                element = self.driver.find_element("css selector", locator)
                element.click()
        time.sleep(2)
        confirm_page = check_out_page.clickButtonCheckOut()
        #log.info("Entering country name as india")
        btn_success = confirm_page.buttonSuccess()
        btn_success.click()
        input_country = confirm_page.SelectCountry()
        input_country.send_keys("India")
        time.sleep(5)
        suggestions = confirm_page.suggestCountry()
        suggestions.click()
        time.sleep(3)
        checkbox_primary = confirm_page.selectCheckboxPrimary()
        checkbox_primary.click()
        submit = confirm_page.SubmitForm()
        submit.click()
        self.driver.get_screenshot_as_file("screen.png")
        success_message = confirm_page.successMessage()
        message = success_message.text
        log.info("Text received from application is "+message)
        assert expected_message == message
