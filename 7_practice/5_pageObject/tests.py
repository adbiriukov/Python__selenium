from itera_page import IteraPage


def test_itera_enter_text_fields(browser):
    itera_automation_page = IteraPage(browser)
    itera_automation_page.go_to_site()
    # takes 5 arguments: name, phone, email, password, address
    itera_automation_page.enter_words('name', 'phone', 'email', 'password', 'address')


# CheckBox & Radio Button practice
# Radio: 'female', 'male' Checkboxes: 'monday', 'wednesday', 'friday'
def test_itera_checkbox_radio_button(browser):
    itera_automation_page = IteraPage(browser)
    itera_automation_page.go_to_site()
    # choose radio button
    radio_female = itera_automation_page.choose_radio_button_by_id('female')
    radio_female.is_selected()
    # choose checkboxes
    checkbox_monday = itera_automation_page.choose_radio_button_by_id('monday')
    checkbox_friday = itera_automation_page.choose_radio_button_by_id('friday')
    checkbox_monday.is_selected()
    checkbox_friday.is_selected()


def test_itera_dropdown(browser):
    itera_automation_page = IteraPage(browser)
    itera_automation_page.go_to_site()
    # Enter visible text for drop down menu
    dropdown_result = itera_automation_page.choose_dropdown('Norway')
    assert dropdown_result == 'Norway'


def test_itera_checkbox_radio_button_by_id(browser):
    itera_automation_page = IteraPage(browser)
    itera_automation_page.go_to_site()
    # choose radio button
    radio_xpath = itera_automation_page.choose_radio_button_by_xpath('/html/body/div/div[5]/div[2]/div[1]/div[2]/label')
    radio_xpath.is_selected()
    # choose checkboxes
    checkbox_selenium = itera_automation_page.choose_radio_button_by_xpath('/html/body/div/div[5]/div[2]/div[2]/div[1]/label')
    checkbox_serenity = itera_automation_page.choose_radio_button_by_xpath('/html/body/div/div[5]/div[2]/div[2]/div[4]/label')
    checkbox_selenium.is_selected()
    checkbox_serenity.is_selected()
