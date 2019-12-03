from selenium import webdriver
import time
import pytest
from PageObjects.test_loginpage import TestLoginPage
from PageObjects.test_HomePageSearch import TestHomepage
import xlrd
import xlwt
from TestData.test_XLUtility import TestXLUtility
import allure
from allure_commons.types import AttachmentType


class GuestDetailsPage:

    def __init__(self, driver):
        self.driver = driver
        self.First_Name = '//*[@id=" 41630_0_first"]'
        self.Last_Name = '//*[@id=" 41630_0_last"]'
        self.Email = '//*[@id=" 41631_0"]'
        self.Confirm_Email = '//*[@id=" 41631_0_confirm"]'
        self.Phone = '//*[@class="input-placeholder"]'
        self.Phone_click ='//*[@type="tel"]'
        self.Card_Nbr ='//*[@id="card-number"]'
        self.Card_HolderName ='//*[@id="card-name"]'
        self.Expiry_date = '//*[@id="card-expiry"]'
        self.Cvv_Nbr ='//*[@id="card-cvv"]'
        self.Complete_booking_btn ='//*[@class="book-now-wrapper"]'

    def Entr_FirstName(self):
        self.driver.find_element_by_xpath(self.First_Name)
    def Entr_LastName(self):
        self.driver.find_element_by_xpath(self.Last_Name)
    def Entr_Email(self):
        self.driver.find_element_by_xpath(self.Email)
    def Entr_ConfirmEmail(self):
        self.driver.find_element_by_xpath(self.Confirm_Email)
    def Enter_PhoneNbr(self):
        self.driver.find_element_by_xpath(self.Phone_click)

    def Enter_CardNbr(self):
        self.driver.find_element_by_xpath(self.Phone_click)
    def Enter_CardHolderName(self):
        self.driver.find_element_by_xpath(self.Phone_click)
    def Enter_ExpiryDate(self):
        self.driver.find_element_by_xpath(self.Phone_click)
    def Enter_CvvNbr(self):
        self.driver.find_element_by_xpath(self.Phone_click)
