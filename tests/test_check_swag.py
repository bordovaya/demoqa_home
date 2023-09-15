from conftest import browser
from pages.swag_labs import SwagLabs

def test_icon_exist(browser):
    demo_page = SwagLabs(browser)
    demo_page.visit()
    assert demo_page.exist_icon()
    assert demo_page.exist_form_name()
    assert demo_page.exist_form_password()
