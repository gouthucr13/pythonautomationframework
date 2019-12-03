class TestLoginPage:

    def __init__(self, driver):
        self.driver = driver

        # self.username_textbox_id = "ctl00_cpMain_UcLogin1_LoginC_UserName"
        # self.password_textbox_id = "ctl00_cpMain_UcLogin1_LoginC_Password"
        # self.login_button_id = "ctl00_cpMain_UcLogin1_LoginC_cmdSubmit"
        # self.login_errormessage_id = "ctl00_cpMain_UcLogin1_LoginC_lblError"
        self.List_AvailableDates = "//*[@class='date-big-wrapper   ']"
        self.Balcony_seat = '//*[contains (@id, "SE-BALCONY-") and @bookable="true"]'
        self.UpperCircle_seat = '//*[contains (@id, "SE-UPPERCIRCLE-") and @bookable="true"]'
        self.DressCircle_seat = '//*[contains (@id, "SE-DRESSCIRCLE-") and @bookable="true"]'
        self.Stall_seat = '//*[contains (@id, "SE-STALLS-") and @bookable="true"]'
        self.Next_btn ='//*[@class="next-button selectable"]'

    def Select_Date(self):
        Get_DatesList = self.driver.find_elements_by_id(self.driver.List_AvailableDates)
        for element in Get_DatesList:
           element.click()
           break

    def select_Balcony_seat(self):
        Get_BalconyList= self.driver.find_elements_by_id(self.driver.List_AvailableDates)
        for Balconyseat in Get_BalconyList:
            Balconyseat.click()
            break

    def select_Uppercircle_seat(self):
        Get_UppercircleList = self.driver.find_elements_by_id(self.driver.List_AvailableDates)
        for Uppercicrcleseat in Get_UppercircleList:
            Uppercicrcleseat.click()
            break

    def select_Dresscircle_seat(self):
        Get_DressCircleList = self.driver.find_elements_by_id(self.driver.List_AvailableDates)
        for DressCircleseat in Get_DressCircleList:
            DressCircleseat.click()
            break

    def select_Stall_seat(self):
        Get_StallList = self.driver.find_elements_by_id(self.driver.List_AvailableDates)
        for Stallseat in Get_StallList:
            Stallseat.click()
            break

    def Amount_next_btn(self):
        self.driver.find_element_by_xpath(self.Next_btn).click()

    # def enter_password(self, password):
    #     self.driver.find_element_by_id(self.password_textbox_id).clear()
    #     self.driver.find_element_by_id(self.password_textbox_id).send_keys(password)
    #
    # def click_login(self):
    #     self.driver.find_element_by_id(self.login_button_id).click()
    #
    # def get_invalidmessage(self):
    #     if self.driver.find_element_by_id(self.login_errormessage_id).text == "Please try again.":
    #         print("Invalid test case is PASSED")
    #         assert self.driver.find_element_by_id(self.login_errormessage_id).text == "Please try again."
    #     else:
    #         print("Invalid test case is FAILED")
    #         assert self.driver.find_element_by_id(self.login_errormessage_id).text == "Please try again."







