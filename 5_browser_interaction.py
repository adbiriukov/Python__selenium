def test_search(self):
    search_field = self.driver.find_element_by_name("q")
    search_field.clear()
    # check maxlength attribute is set to 2048
    self.assertEqual("2048", search_field.get_attribute("maxlength"))
    search_field.send_keys("phones")
    search_field.submit()
    time.sleep(1)
    assert "phones" in self.driver.title