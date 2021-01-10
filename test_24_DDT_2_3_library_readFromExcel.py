import xlrd, unittest
from ddt import ddt, data, unpack
from selenium import webdriver


def get_data(file_name):
    rows = []
    data_file = xlrd.open_workbook(file_name)
    # get the first sheet in xlsx file
    sheet = data_file.sheet_by_index(0)
    # iterate through the sheet and get data from rows in list
    # 0 is for line from where to start
    for row_idx in range(0, sheet.nrows):
        rows.append(list(sheet.row_values(row_idx, 0, sheet.ncols)))
    return rows


@ddt
class SeacrhExcelDDT(unittest.TestCase):
    def setUp(self):
        # create a new firefox sessopm
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('https://www.amazon.com/')
    # for some reason xlsx files currently not supported by xlrd
    @data(*get_data('./selenium_logs/xlsx_files/ddt_file.xls'))
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
