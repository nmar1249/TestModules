from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class GeicoVehicleTest:

    driver = webdriver
    CurrentModule = ""
    ErrorCount = 0

    def __init__(self):
        self.driver = webdriver.Chrome(r"C:\Users\NickMarine\PycharmProjects\test\drivers\chromedriver.exe")
        self.CurrentModule = "Initialization"
        self.ErrorCount = 0

    def enter_name(self):
        try:
            self.CurrentModule = "enter_name"
            # enter first and last name
            time.sleep(2)

            FirstNameInput0 = self.driver.find_element_by_xpath("//input[@id='firstName']")
            ActionChains(self.driver).move_to_element(FirstNameInput0).click().send_keys("Hello").send_keys(Keys.TAB).send_keys(
                "World").send_keys(Keys.TAB).send_keys(Keys.ENTER).perform()
        except Exception as err:
            self.error_message(err)

    def skip_help_page(self):
        try:
            self.CurrentModule = "skip_help_page"
            # skip the initial "how can we help" page
            time.sleep(2)

            ZipInput0 = self.driver.find_element_by_xpath("//input[@id='zip']")
            ActionChains(self.driver).move_to_element(ZipInput0).click().send_keys("60103").send_keys(
                Keys.TAB).send_keys(
                Keys.ENTER).perform()

            time.sleep(2)
            butbar = self.driver.find_element_by_class_name("button-bar")

            SkipA0 = butbar.find_element_by_class_name("skip-collect-intent.link--primary")

            ActionChains(self.driver).move_to_element(SkipA0).click().perform()

            self.go_next()
        except Exception as err:
            self.error_message(err)

    def enter_DOB(self):
        try:
            self.CurrentModule = "enter_DOB"
            # enter DOB
            time.sleep(2)

            MonthDOB0 = self.driver.find_element_by_xpath("//input[@id='date-monthdob']")
            ActionChains(self.driver).move_to_element(MonthDOB0).click().send_keys("06").perform()

            DayDOB0 = self.driver.find_element_by_xpath("//input[@id='date-daydob']")
            ActionChains(self.driver).move_to_element(DayDOB0).click().send_keys("06").perform()

            YearDOB0 = self.driver.find_element_by_xpath("//input[@id='date-yeardob']")
            ActionChains(self.driver).move_to_element(YearDOB0).click().send_keys("1996").send_keys(Keys.TAB).send_keys(
                Keys.ENTER).perform()
        except Exception as err:
            self.error_message(err)

    def enter_address(self):
        try:
            self.CurrentModule = "enter_address"
            # enter street address info
            time.sleep(2)

            StreetInput0 = self.driver.find_element_by_xpath("//input[@id='street']")
            ActionChains(self.driver).move_to_element(StreetInput0).click().send_keys("123 Whatever St.").perform()

            AptInput0 = self.driver.find_element_by_xpath("//input[@id='apt']")
            ActionChains(self.driver).move_to_element(AptInput0).click().send_keys("312").perform()

            ZipInput1 = self.driver.find_element_by_xpath("//input[@id='zip']")
            ActionChains(self.driver).move_to_element(ZipInput1).click().send_keys("60103").send_keys(Keys.TAB).send_keys(
                Keys.ENTER).perform()

        except Exception as err:
            self.error_message(err)

    def verify_address(self):
        try:
            self.CurrentModule = "verify_address"
            # verify address
            time.sleep(7)

            OriginalAddressLabel0 = self.driver.find_element_by_xpath("//label[@for='originalAddress']")
            ActionChains(self.driver).move_to_element(OriginalAddressLabel0).click().send_keys(Keys.TAB).send_keys(
                Keys.ENTER).perform()
        except Exception as err:
            self.error_message(err)

    def have_you_moved(self):
        # have you moved in the last 2 months (put no)
        try:
            self.CurrentModule = "have_you_moved"
            time.sleep(6)
            HasMovedInLast2MonthsLabel1 = self.driver.find_element_by_xpath("//label[@for='hasMovedInLast2Months1']")
            ActionChains(self.driver).move_to_element(HasMovedInLast2MonthsLabel1).click().send_keys(Keys.TAB).send_keys(
                Keys.ENTER).perform()
        except Exception as err:
            self.error_message(err)

    def go_next(self):
        try:
            self.CurrentModule = "go_next"
            time.sleep(1)
            NextButton0 = self.driver.find_element_by_xpath("//button[contains(text(), 'Next')]")
            ActionChains(self.driver).move_to_element(NextButton0).click().click().perform()
        except Exception as err:
            self.error_message(err)


    # only use this to pass through this stage, not good for testing functionality
    # indices available is reliant on the previous elements
    def select_specific_vehicle(self, year_index, make_index, model_index):
        try:
            self.CurrentModule = "select_specific_vehicle"
            time.sleep(4)
            VehicleYearSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='vehicleYear']"))
            VehicleYearSelect0.select_by_index(year_index)
            time.sleep(1)
            VehicleMakeSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='vehicleMake']"))
            VehicleMakeSelect0.select_by_index(make_index)
            time.sleep(1)
            VehicleModelSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='vehicleModel']"))
            VehicleModelSelect0.select_by_index(model_index)

            self.go_next()

        except Exception as err:
            self.error_message_vehicle(err, year_index, make_index, model_index)

    def select_vehicles(self):

        self.CurrentModule = "select_vehicles"

        ### NOW WE CAN TEST FOR THE ADDING OF VEHCILES ###
        time.sleep(4)

        VehicleYearSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='vehicleYear']"))

        YearOption = 0

        while YearOption < len(VehicleYearSelect0.options) - 1:
            try:
                VehicleYearSelect0.select_by_index(YearOption)
            except:
                VehicleYearSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='vehicleYear']"))
                VehicleYearSelect0.select_by_index(YearOption)

            time.sleep(1)
            VehicleMakeSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='vehicleMake']"))

            MakeOption = 1
            while MakeOption < len(VehicleMakeSelect0.options):
                try:
                    VehicleMakeSelect0.select_by_index(MakeOption)
                except:
                    VehicleMakeSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='vehicleMake']"))
                    VehicleMakeSelect0.select_by_index(MakeOption)

                time.sleep(1)
                VehicleModelSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='vehicleModel']"))

                ModelOption = 1
                while ModelOption < len(VehicleModelSelect0.options):  # it really starts to slow down over here
                    try:
                        VehicleModelSelect0.select_by_index(ModelOption)
                    except:
                        VehicleModelSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='vehicleModel']"))
                        VehicleModelSelect0.select_by_index(ModelOption)

                    # time.sleep(1)
                    ModelOption = ModelOption + 1
                MakeOption = MakeOption + 1
            YearOption = YearOption + 1

    def add_vehicle_pre1981(self, year, make, model):
        try:
            self.CurrentModule = "add_vehicle_pre1981"

            VehicleYearSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='vehicleYear']"))
            VehicleYearSelect0.select_by_index(len(VehicleYearSelect0.options) - 1)

            ActualVehicleYearInput0 = self.driver.find_element_by_xpath("//input[@id='actualVehicleYear']")
            ActionChains(self.driver).move_to_element(ActualVehicleYearInput0).click().send_keys(str(year)).perform()

            OtherMakeInput0 = self.driver.find_element_by_xpath("//input[@id='otherMake']")
            ActionChains(self.driver).move_to_element(OtherMakeInput0).click().send_keys(str(make)).perform()

            OtherModelInput0 = self.driver.find_element_by_xpath("//input[@id='otherModel']")
            ActionChains(self.driver).move_to_element(OtherModelInput0).click().send_keys(str(model)).perform()

            self.go_next()
        except Exception as err:
            self.error_message_vehicle(err, year, make, model)

    def select_antitheft_devices(self):
        try:
            self.CurrentModule = "select_antitheft_devices"

            time.sleep(3)
            AntiTheftDeviceSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='antiTheftDevice']"))

            ATDOption = 0

            while ATDOption < len(AntiTheftDeviceSelect0.options):
                AntiTheftDeviceSelect0.select_by_index(ATDOption)
                ATDOption = ATDOption + 1
        except Exception as err:
            self.error_message(err)

    # index guide
    # 0 = no anti theft, 1 = alarm only/active disabling device, 2 = passive disabling device
    def select_specific_antitheft_device(self, index):
        try:
            self.CurrentModule = "select_specific_antitheft_device"
            time.sleep(3)
            AntiTheftDeviceSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='antiTheftDevice']"))
            AntiTheftDeviceSelect0.select_by_index(index)

            self.go_next()
        except Exception as err:
            self.error_message(err)

    # index guide
    # 0 = owned, 1 = financed, 2 = leased
    def select_ownership(self, index):
        try:
            self.CurrentModule = "select_ownership"
            time.sleep(3)

            if index == 0:
                VehicleOwned0 = self.driver.find_element_by_xpath("//label[@for='vehicleOwned0']")
                ActionChains(self.driver).move_to_element(VehicleOwned0).click().perform()
            if index == 1:
                VehicleOwned1 = self.driver.find_element_by_xpath("//label[@for='vehicleOwned1']")
                ActionChains(self.driver).move_to_element(VehicleOwned1).click().perform()
            if index == 2:
                VehicleOwned2 = self.driver.find_element_by_xpath("//label[@for='vehicleOwned2']")
                ActionChains(self.driver).move_to_element(VehicleOwned2).click().perform()

            self.go_next()

        except Exception as err:
            self.error_message(err)

    # index guide
    # 0 = commute, 1 = pleasure, 2 = business
    def select_primary_use(self, index):
        try:

            self.CurrentModule = "select_primary_use"
            time.sleep(3)

            if index == 0:
                PrimaryUse0 = self.driver.find_element_by_xpath("//label[@for='primaryUse0']")
                ActionChains(self.driver).move_to_element(PrimaryUse0).click().perform()
                self.primary_use_commute(1, 200)
            if index == 1:
                PrimaryUse1 = self.driver.find_element_by_xpath("//label[@for='primaryUse1']")
                ActionChains(self.driver).move_to_element(PrimaryUse1).click().perform()
                self.go_next()
            if index == 2:
                PrimaryUse2 = self.driver.find_element_by_xpath("//label[@for='primaryUse2']")
                ActionChains(self.driver).move_to_element(PrimaryUse2).click().perform()
                self.primary_use_business(1)

        except Exception as err:
            self.error_message(err)

    # menu options for commuting
    def primary_use_commute(self, index, miles):
        try:
            self.CurrentModule = "primary_use_commute"
            time.sleep(1)
            DaysDrivenSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='daysDriven']"))
            DaysDrivenSelect0.select_by_index(index)

            MilesDrivenInput0 = self.driver.find_element_by_xpath("//input[@id='milesDriven']")
            ActionChains(self.driver).move_to_element(MilesDrivenInput0).click().send_keys(str(miles)).perform()

            self.go_next()

        except Exception as err:
            self.error_message(err)


    def select_annual_mileage(self, index):
        try:
            self.CurrentModule = "select_annual_mileage"
            time.sleep(3)
            AnnualMileageSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='annualMileage']"))
            AnnualMileageSelect0.select_by_index(index)

            self.go_next()

        except Exception as err:
            self.error_message(err)

    def primary_use_business(self, index):
        try:
            self.CurrentModule = "primary_use_business"
            time.sleep(1)
            TypeOfBusinessUseSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='typeOfBusinessUse']"))
            TypeOfBusinessUseSelect0.select_by_index(index)

            self.go_next()
        except Exception as err:
            self.error_message(err)

    def select_body_styles(self):
        try:
            self.CurrentModule = "select_body_styles"
            time.sleep(1)

            BodyStylesSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='bodyStyles']"))

            BSSOption = 0
            while BSSOption < len(BodyStylesSelect0.options):
                BodyStylesSelect0.select_by_index(BSSOption)
                BSSOption = BSSOption + 1

        except Exception as err:
            self.error_message(err)

    def select_specific_body_style(self, index):
        try:
            self.CurrentModule = "select_specific_body_styles"
            time.sleep(1)

            BodyStylesSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='bodyStyles']"))

            BodyStylesSelect0.select_by_index(index)

            self.go_next()
        except Exception as err:
            self.error_message(err)

    def select_new_costs(self):

        try:
            self.CurrentModule = "select_new_costs"
            time.sleep(1)

            CostNewValueSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='costNewValue']"))

            CNVSOption = 0
            while CNVSOption < len(CostNewValueSelect0.options):
                CostNewValueSelect0.select_by_index(CNVSOption)
                CNVSOption = CNVSOption + 1

        except Exception as err:
            self.error_message(err)

    def select_specific_new_costs(self, index):

        try:
            self.CurrentModule = "select_specific_new_costs"
            time.sleep(1)

            CostNewValueSelect0 = Select(self.driver.find_element_by_xpath("//select[@id='costNewValue']"))
            CostNewValueSelect0.select_by_index(index)

            self.go_next()
        except Exception as err:
            self.error_message(err)

    def select_antilock_brakes(self, index):
        try:

            self.CurrentModule = "select_antilock_brakes"
            time.sleep(3)

            if index == 0:
                AntilockBrakesLabel0 = self.driver.find_element_by_xpath("//label[@for='hasAntilockBrakes0']")
                ActionChains(self.driver).move_to_element(AntilockBrakesLabel0).click().perform()
                self.go_next()
            if index == 1:
                AntilockBrakesLabel1 = self.driver.find_element_by_xpath("//label[@for='hasAntilockBrakes1']")
                ActionChains(self.driver).move_to_element(AntilockBrakesLabel1).click().perform()
                self.go_next()

        except Exception as err:
            self.error_message(err)

    def get_to_vehicle_page(self):
        self.driver.get("https://www.geico.com/")
        time.sleep(2)
        self.skip_help_page()
        self.enter_name()
        self.enter_DOB()
        self.enter_address()
        self.verify_address()
        self.have_you_moved()

    def error_message(self, err):
        self.ErrorCount = self.ErrorCount + 1
        print("Exception thrown on module:\t" + str(self.CurrentModule))
        print(str(err))
        print("Error Count:\t" + str(self.ErrorCount))

    def error_message_vehicle(self, err, year, make, model):
        self.error_message(err)
        print("Year:\t" + str(year) + " Make:\t" + str(make) + " Model:\t" + str(model))