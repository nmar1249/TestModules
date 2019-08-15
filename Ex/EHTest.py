from selenium import webdriver
from selenium.webdriver.support.ui import Select


class EHTest:

    year = 1901
    day = 1
    month = 1
    driver = webdriver

    def __init__(self, y, d, m):
        self.year = y
        self.day = d
        self.month = m
        self.driver = webdriver.Chrome(r"C:\Users\NickMarine\PycharmProjects\test\drivers\chromedriver.exe")
        # ^^ this allows the program to stay on a single window ^^

    def get_year(self):
        return self.year

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def set_year(self, y):
        self.year = y

    def set_day(self, d):
        self.day = d

    def set_month(self, m):
        self.month = m

    # checks the date and corrects it if needed (i.e. if you are on month 13, itll go to month 1 and add 1 to year)
    def verify_dates(self):
        if int(self.day) > 31:
            self.set_day(1)
            self.set_month(int(self.month) + 1)
        if int(self.month) > 12:
            self.set_month(1)
            self.set_year(int(self.year) + 1)


    def inc(self, n):
        return int(n) + 1


    def loop(self):
        self.driver.get('https://www.yelp.com/signup')

        self.driver.maximize_window()
        monthButton = Select(self.driver.find_element_by_name('birthdate_m'))
        yearButton = Select(self.driver.find_element_by_name('birthdate_y'))
        dayButton = Select(self.driver.find_element_by_name('birthdate_d'))

        self.verify_dates()

        while int(self.year) < 2019:
            self.year = str(self.year)
            yearButton.select_by_value(self.year)
            while int(self.month) < 16:
                self.month = str(self.month)
                monthButton.select_by_value(self.month)
                while int(self.day) < 33:
                    self.day = str(self.day)
                    dayButton.select_by_value(self.day)
                    self.day = self.inc(self.day)
                self.month = self.inc(self.month)
            self.year = self.inc(self.year)
