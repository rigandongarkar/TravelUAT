import XLUtils
from PageObjects.signupObjects import SignupObjectClass
from framework.BaseClass import Base_Class


class Test_SignUp(Base_Class):

    def test_SignupUsers(self):
        SignUp_Object = SignupObjectClass(self.driver)
        SignUp_Object.SignUp_ButtonClick().click()
        path = "C:\\Users\\rigan\\PycharmProjects\\travelTest\\Signupusers.xlsx"

        rows = XLUtils.getRowCount(path, "Sheet1")
        for r in range(2, rows+1):
            firstname = XLUtils.readData(path, "Sheet1", r, 1)
            lastname = XLUtils.readData(path, "Sheet1", r, 2)
            phone = XLUtils.readData(path, "Sheet1", r, 3)
            email = XLUtils.readData(path, "Sheet1", r, 4)
            password = XLUtils.readData(path, "Sheet1", r, 5)

            SignUp_Object.FirstNameValue().send_keys(firstname)
            SignUp_Object.LastName().send_keys(lastname)
            SignUp_Object.PhoneNumber().send_keys(phone)
            SignUp_Object.EmailID().send_keys(email)
            SignUp_Object.Password().send_keys(password)
            # self.driver.find_element_by_xpath("//span[@title='Customer']").click()
            SignUp_Object.SubmitButton().click()
            SignUp_SuccessText = SignUp_Object.FinalSuccessTextMessage().text
            if "successfull" in SignUp_SuccessText:
                XLUtils.writeData(path, "Sheet1", r, 6, "Signup is Successfull")
            else:
                XLUtils.writeData(path, "Sheet1", r, 6, "Signup Failed")

            SignUp_Object.HomePageRedirection().click()
            SignUp_Object.SignUpInsideLoop().click()

