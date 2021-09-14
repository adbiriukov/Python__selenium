from hero_pages import HeroPages
import pytest
import time

# def test_hero_add_remove_elements(browser):
#     hero_automation_page = HeroPages(browser)
#     hero_automation_page.go_to_site()
#     # Open 'Add/Remove Elements' page
#     hero_automation_page.open_page_by_xpath(2)
#     # Check that Add/Remove bts working
#     a = hero_automation_page.page_add_remove_elements()
#     for x in a:
#         assert x is True
#         print(x)


# def test_hero_add_remove_elements(browser):
#     hero_automation_page = HeroPages(browser)
#     # Open 'Basic Auth' page and check that element is present
#     assert hero_automation_page.enter_login_and_password() is True


# @pytest.mark.xfail
# def test_find_broken_images(browser):
#     hero_automation_page = HeroPages(browser)
#     hero_automation_page.go_to_site()
#     # Open page with broken images
#     hero_automation_page.open_page_by_xpath(4)
#
#     broken_images = hero_automation_page.find_broken_images()
#     if broken_images is []:
#         assert True
#     else:
#         for x in broken_images:
#             print(x + " is broken.")
#         assert False

# def test_checkboxes(browser):
#     hero_automation_page = HeroPages(browser)
#     hero_automation_page.go_to_site()
#     # Open checkboxes page
#     hero_automation_page.open_page_by_xpath(6)
#     assert hero_automation_page.select_checkboxes() is True

# def test_context_menu(browser):
#     hero_automation_page = HeroPages(browser)
#     hero_automation_page.go_to_site()
#     # Open context menu page
#     hero_automation_page.open_page_by_xpath(7)
#     hero_automation_page.context_menu()

# def test_digest_auth(browser):
#     hero_automation_page = HeroPages(browser)
#     hero_automation_page.go_to_site()
#     # Open digest auth page
#     hero_automation_page.open_page_by_xpath(8)
#     hero_automation_page.enter_login_and_password()


# def test_disappearing_elements(browser):
#     hero_automation_page = HeroPages(browser)
#     hero_automation_page.go_to_site()
#     # Open page
#     hero_automation_page.open_page_by_xpath(9)
#     assert hero_automation_page.disappearing_elements() is True

# def test_drag_and_drop(browser):
#     hero_automation_page = HeroPages(browser)
#     hero_automation_page.go_to_site()
#     # Open page
#     hero_automation_page.open_page_by_xpath(10)
#     hero_automation_page.drag_and_drop()

# def test_dropdown_menu(browser):
#     hero_automation_page = HeroPages(browser)
#     hero_automation_page.go_to_site()
#     # Open page
#     hero_automation_page.open_page_by_xpath(11)
#     # Visible text: Option 1 or Option 2
#     assert hero_automation_page.drop_down_menu('Option 2') == 'Option 2'

def test_dynamic_content(browser):
    hero_automation_page = HeroPages(browser)
    hero_automation_page.go_to_site()
    # Open page
    hero_automation_page.open_page_by_xpath(12)
    assert hero_automation_page.dynamic_content() is True





