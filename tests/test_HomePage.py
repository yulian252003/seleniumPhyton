import pytest
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass
import time


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        log.info("First name is: " + getData["firstname"])
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
        homepage.getPassword().send_keys("3212141352Jpm*")
        homepage.selectCheck().click()
        homepage.selectStatus().click()
        sel = Select(homepage.selectGender())
        sel.select_by_visible_text(getData["gender"])
        time.sleep(5)
        homepage.selectSubmit().click()
        message = homepage.reviewMessage().text

        assert "Success" in message
        self.driver.refresh()

        # @pytest.fixture(params=[("Rahul", "shetty", "Male"), ("Andrea", "Rios", "Female")])

    # @pytest.fixture(params=HomePageData.test_HomePage_data)
    @pytest.fixture(params=HomePageData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
