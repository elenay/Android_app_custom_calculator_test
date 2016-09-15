import unittest
from appium import webdriver
from screen import CalculatorScreen


class ContactsAndroidTests(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['app'] = "C:\\Users\\magic\\Documents\\Calc\\app\\build\\outputs\\apk\\app-debug.apk"

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.page = CalculatorScreen(self.driver)

    def test_deduct(self):
        result = self.page.deduction('1', '2')
        self.assertEqual('-1', result.text)

    def test_divide_int_result(self):
        result = self.page.division('4', '2')
        self.assertEqual('2', result.text)

    def test_divide_float_result(self):
        result = self.page.division('4', '5')
        self.assertEqual('0.8', result.text)

    def test_deduct_float(self):
        result = self.page.deduction('0,5', '4')
        self.assertEqual('3,5', result.text)

    def test_empty_both_args(self):
        result = self.page.deduction('', '')
        self.assertEqual('', result.text)

    def test_empty_first_arg(self):
        result = self.page.division('', '5')
        self.assertEqual('', result.text)

    def test_empty_second_arg(self):
        result = self.page.division('7', '')
        self.assertEqual('', result.text)

    def test_division_by_zero(self):
        result = self.page.division('5', '0')
        self.assertEqual('error', result.text)

    def test_negative_values(self):
        result = self.page.deduction('-6', '-2')
        self.assertEqual('4', result.text)

    def test_text_args(self):
        result = self.page.division('abc', 'bca')
        self.assertEqual('', result.text)

    def tearDown(self):
        self.driver.quit()

suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
unittest.TextTestRunner(verbosity=2).run(suite)