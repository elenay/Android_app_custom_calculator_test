
class CalculatorScreen():

    def __init__(self, driver):
        self.driver = driver

    def find_element_one(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_android_uiautomator('new UiSelector().description("arg1")')

    def find_element_two(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_android_uiautomator('new UiSelector().description("arg2")')

    def click_deduct(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_android_uiautomator('new UiSelector().description("subtraction")').click()

    def click_divide(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_android_uiautomator('new UiSelector().description("division")').click()

    def result_field(self):
        self.driver.implicitly_wait(10)
        return self.driver.find_element_by_android_uiautomator('new UiSelector().description("result")')

    def deduction(self, a1, a2):
        self.find_element_one().send_keys(a1)
        self.find_element_two().send_keys(a2)
        self.click_deduct()
        return self.result_field()

    def division(self, a1, a2):
        self.find_element_one().send_keys(a1)
        self.find_element_two().send_keys(a2)
        self.click_divide()
        return self.result_field()