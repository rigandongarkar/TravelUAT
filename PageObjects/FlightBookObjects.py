from selenium.webdriver.common.by import By


class FlightBook:

    def __init__(self, driver):
        self.driver = driver

    hotelsearchclick = (By.XPATH, "//span[@id='select2-hotels_city-container']")
    # self.driver.find_element_by_xpath("//span[@id='select2-hotels_city-container']")

    location_value = (By.XPATH, "//input[@class='select2-search__field']")
    # self.driver.find_element_by_xpath("//input[@class='select2-search__field']")

    def HotelSeachClick(self):
        return self.driver.find_element(*FlightBook.hotelsearchclick)

    def Location(self):
        return self.driver.find_element(*FlightBook.location_value)