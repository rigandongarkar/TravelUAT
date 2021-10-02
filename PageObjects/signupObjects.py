from selenium.webdriver.common.by import By


class SignupObjectClass:

    def __init__(self, driver):
        self.driver = driver

    SignUp_Button_Click_element = (By.LINK_TEXT, "Signup")
    # self.driver.find_element_by_link_text("Signup")

    firstname_obj = (By.NAME, "first_name")
    # self.driver.find_element_by_name("first_name")

    lastname_obj = (By.NAME, "last_name")

    phoneno_obj = (By.NAME, "phone")

    emailid_obj = (By.NAME, "email")

    passwd_obj = (By.NAME, "password")

    Submit_Button_Click = (By.XPATH, "//button[@type='submit']")
    # self.driver.find_element_by_xpath("//button[@type='submit']")

    FinalSuccessText = (By.XPATH, "//div[contains(@class,'alert-success signup')]")
    # self.driver.find_element_by_xpath("//div[contains(@class,'alert-success signup')]")

    HomePage_Redirect = (By.LINK_TEXT, "Home")
    # self.driver.find_element_by_link_text("Home")

    SignUp_Button_Click_element_two = (By.LINK_TEXT, "Signup")
    # self.driver.find_element_by_link_text("Signup")

    def SignUp_ButtonClick(self):
        return self.driver.find_element(*SignupObjectClass.SignUp_Button_Click_element)

    def FirstNameValue(self):
        return self.driver.find_element(*SignupObjectClass.firstname_obj)

    def LastName(self):
        return self.driver.find_element(*SignupObjectClass.lastname_obj)

    def PhoneNumber(self):
        return self.driver.find_element(*SignupObjectClass.phoneno_obj)

    def EmailID(self):
        return self.driver.find_element(*SignupObjectClass.emailid_obj)

    def Password(self):
        return self.driver.find_element(*SignupObjectClass.passwd_obj)

    def SubmitButton(self):
        return self.driver.find_element(*SignupObjectClass.Submit_Button_Click)

    def FinalSuccessTextMessage(self):
        return self.driver.find_element(*SignupObjectClass.FinalSuccessText)

    def HomePageRedirection(self):
        return self.driver.find_element(*SignupObjectClass.HomePage_Redirect)

    def SignUpInsideLoop(self):
        return self.driver.find_element(*SignupObjectClass.SignUp_Button_Click_element_two)