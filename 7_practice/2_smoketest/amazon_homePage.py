import unittest
from selenium import webdriver
from amazon_web_elements import WebElements


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        cls.driver.implicitly_wait(5)
        cls.driver.maximize_window()
        cls.driver.get("https://www.amazon.com/")

    def test_search_field_is_displayed(self):
        # check search field exists on  page
        self.assertTrue(self.driver.find_element(*WebElements.search_field).is_displayed())

    def test_search_field_is_enabled(self):
        # check search field exists on  page
        self.assertTrue(self.driver.find_element(*WebElements.search_field).is_enabled())

    def test_search_field_attribute(self):
        search_field = self.driver.find_element(*WebElements.search_field)
        # assert that search field don't have attribute max length
        self.assertFalse(search_field.get_attribute('maxlength'))

    def test_my_account_link_is_displayed(self):
        account_link = self.driver.find_element_by_link_text('Amazon Devices')
        # check Amazon Devices link is displayed/visible in the Home page footer
        self.assertTrue(account_link.is_displayed())

    def test_count_of_promo_banners_images(self):
        # get promo banner list
        banner_list = self.driver.find_element(*WebElements.banner_list)

        # get images from the banner_list
        banners = banner_list.find_elements_by_tag_name('img')

        # check there are 5 banners displayed on the page
        self.assertEqual(5, len(banners))

    def test_language_option_is_displayed(self):
        # check deliver to country is displayed
        self.assertTrue(self.driver.find_element(*WebElements.deliver_country).is_displayed())

    def test_shopping_cart_empty_message(self):
        # check content of Shopping Cart is empty
        cart_status = self.driver.find_element(*WebElements.cart).get_attribute('aria-label')
        self.assertEqual(cart_status, '0 items in cart')

    @classmethod
    def tearDown(cls):
        # close the browser window
        cls.driver = webdriver.Chrome(executable_path="../../chromedriver.exe")
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
