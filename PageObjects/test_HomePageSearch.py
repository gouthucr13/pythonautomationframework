from selenium import webdriver
import time
import pytest
#from PageObjects.test_loginpage import TestLoginPage
#from PageObjects.test_HomePageSearch import TestHomepage
import xlrd
import xlwt
from TestData.test_XLUtility import TestXLUtility
import allure
from allure_commons.types import AttachmentType

class TestHomepage:

    global driver
    global path
    path = "C://Users/pbangari/PycharmProjects/git/PythonAutomtionFramework/TestData/test_DataFile.xlsx"

    def __init__(self, driver):
        self.driver = driver

        self.Logo_Icon = "//*[@class='block-logo hide-mobi']"
        self.Search_text = "//*[@id='search-form']/input"
        self.EventName = '//*[@class="title spacer-l-30"]'
        self.Booknow = "//a[@href='https://book.london-theater-tickets.com/book/7233']/div"

    def HomePageLogo(self):
        logoelemet = self.driver.find_element_by_xpath(self.Logo_Icon)

        if logoelemet.is_enabled():
            print("Home page loaded sucessfully")
            allure.attach(driver.get_screenshot_as_png(), name="Logo_Verify_Passed", attachment_type=AttachmentType.PNG)
        else:
            print("Home page is not loaded, Hence Faild")
            allure.attach(driver.get_screenshot_as_png(), name="Logo_Verify_Failed", attachment_type=AttachmentType.PNG)


    def HomePageSearch(self):
        rows = TestXLUtility.getRowCount(path, 'TicketDetail')
        for r in range(2, rows + 1):
            EventName = TestXLUtility.readData(path,"TicketDetail", r, 1)
        self.driver.find_element_by_xpath(self.Search_text_xpath).send_keys(EventName)

    def HomePageEventTitle(self):
       EventText= self.driver.find_element_by_xpath(self.EventName).text

    def HomePageBookNow(self):
        self.driver.find_element_by_xpath(self.Booknow)






