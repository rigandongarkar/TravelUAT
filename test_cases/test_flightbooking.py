import datetime
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

from PageObjects.FlightBookObjects import FlightBook
from framework.BaseClass import Base_Class


class Test_PHPTravels(Base_Class):

    def test_flight_booking_flow(self):
        log = self.getlogger()
        flightBook_Object = FlightBook(self.driver)
        flightBook_Object.HotelSeachClick().click()

        flightBook_Object.Location().send_keys("dubai")
        self.driver.find_element_by_xpath("//*[contains(@class,'select2-results__option--highlighted')]").click()
        self.driver.find_element_by_xpath("//input[@id='checkin']").click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//body/div[4]/div[1]/table/tbody/tr/td")))
        checkindate = self.driver.find_elements(By.XPATH, "//body/div[4]/div[1]/table/tbody/tr/td")
        current_datetime = datetime.datetime.now()
        day = current_datetime.day

        for in_date in checkindate:
            # print(checkin_date.text)
            if in_date.text == str(day + 2):
                in_date.click()
                break
            break

        self.driver.find_element(By.XPATH, "//input[@id='checkin']").click()
        checkoutdate = self.driver.find_elements(By.XPATH, "//body/div[5]/div[1]/table/tbody/tr/td")

        for out_date in checkoutdate:
            if out_date.text == str(day + 6):
                out_date.click()
                break
            break

        # Room Count
        self.driver.find_element(By.CSS_SELECTOR, "span[class='guest_hotels']").click()
        room_count = self.driver.find_element(By.CSS_SELECTOR, "span[class='roomTotal']")
        for count in range(2):  # --- Room Increase
            room_plus = self.driver.find_element(By.XPATH, "//div[@class='roomInc']/i")
            room_plus.click()

        room_minus = self.driver.find_element(By.XPATH, "//div[@class='roomDec']/i")  # --- Room Decrease
        room_minus.click()
        log.debug("Room count : " + room_count.text)

        # People Count-Adults
        people_count = self.driver.find_element(By.CSS_SELECTOR, "span[class='guest_hotels']")
        adult_count = self.driver.find_element(By.XPATH, "//div[@class='row g-1']/div[3]/div/div/div/div/div[2]/div/div/div[2]/i")  # -- Adult Increase
        for count_adlt in range(1):
            adult_count.click()

        adult_minus = self.driver.find_element(By.XPATH, "//div[@class='row g-1']/div[3]/div/div/div/div/div[2]/div/div/div[1]/i")  # -- Adult decrease
        adult_minus.click()

        # People Childs
        child_count = self.driver.find_element(By.XPATH, "//div[@class='row g-1']/div[3]/div/div/div/div/div[3]/div/div/div[2]/i")
        for ccount in range(3):
            child_count.click()
        child_minus = self.driver.find_element(By.XPATH, "//div[@class='row g-1']/div[3]/div/div/div/div/div[3]/div/div/div[1]/i")
        child_minus.click()
        log.debug("People count including Childs : " + people_count.text)

        # nationality
        self.driver.find_element(By.XPATH, "//select[@id='nationality']").click()
        from_nation = self.driver.find_elements(By.XPATH, "//select[@id='nationality']/option")
        random.choice(from_nation).click()

        seach_hotels = self.driver.find_element(By.XPATH, "//form[@id='hotels-search']/div/div/div[4]/div/button")
        seach_hotels.click()

        search_hotels_result = self.driver.find_element(By.XPATH, "//div[@class='breadcrumb-wrap']/div/div/div[2]/div/ul/li").text
        if "Total" in search_hotels_result:
            log.debug("Passed : Hotels Found" + search_hotels_result)
        else:
            log.debug("No Hotel Found")
        # test case ends here