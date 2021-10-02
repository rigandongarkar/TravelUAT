import XLUtils
from framework.BaseClass import Base_Class


class Test_SignUp(Base_Class):

    def test_SignupUsers(self):
        self.driver.find_element_by_link_text("Signup").click()
        path = "C:\\Users\\rigan\\PycharmProjects\\travelTest\\Signupusers.xlsx"

        rows = XLUtils.getRowCount(path, "Sheet1")
        for r in range(2, rows+1):
            firstname = XLUtils.readData(path, "Sheet1", r, 1)
            lastname = XLUtils.readData(path, "Sheet1", r, 2)
            phone = XLUtils.readData(path, "Sheet1", r, 3)
            email = XLUtils.readData(path, "Sheet1", r, 4)
            password = XLUtils.readData(path, "Sheet1", r, 5)

            self.driver.find_element_by_name("first_name").send_keys(firstname)
            self.driver.find_element_by_name("last_name").send_keys(lastname)
            self.driver.find_element_by_name("phone").send_keys(phone)
            self.driver.find_element_by_name("email").send_keys(email)
            self.driver.find_element_by_name("password").send_keys(password)
            # self.driver.find_element_by_xpath("//span[@title='Customer']").click()
            self.driver.find_element_by_xpath("//button[@type='submit']").click()
            SignUp_SuccessText = self.driver.find_element_by_xpath("//div[contains(@class,'alert-success signup')]").text
            if "successfull" in SignUp_SuccessText:
                XLUtils.writeData(path, "Sheet1", r, 6, "Signup is Successfull")
            else:
                XLUtils.writeData(path, "Sheet1", r, 6, "Signup Failed")

            self.driver.find_element_by_link_text("Home").click()
            self.driver.find_element_by_link_text("Signup").click()

