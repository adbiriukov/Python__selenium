import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver


def get_data(file_name):
    # create an empty list to store rows
    rows = []
    # open the CSV file
    data_file = open(file_name, "r")
    # create CSV Reader from CSV file
    reader = csv.reader(data_file)
    # skip the headers
    # next(reader, None)
    # add rows from reader to list
    for row in reader:
        rows.append(row)
    return rows


@ddt
class SeacrhCsvDdt(unittest.TestCase):
    def setUp(self):
        # create a new firefox sessopm
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://www.amazon.com/')

    @data(*get_data('./selenium_logs/CSV/ddt_csv.csv'))
    @unpack
    def test_search(self, search_value, expected_count):
        search_field = self.driver.find_element_by_name('field-keywords')
        search_field.clear()
        search_field.send_keys(search_value)
        search_field.submit()
        result = self.driver.find_element_by_xpath('//*[@id="search"]/span/div/span/h1/div/div[1]/div/div/span[1]')
        print(result.text)
        self.assertTrue(expected_count in result.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
