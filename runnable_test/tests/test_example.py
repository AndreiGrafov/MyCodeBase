import time

from runnable_test.pom.pages.default_page_example import DefaultPage
from runnable_test.pom.pages.form_field import FormField

def test_example(browser):
    default = DefaultPage(browser)
    form_field = FormField(browser)

    # 1 open website
    default.open()

    # select option with fields
    default.click_form_fields()

    # fill in test data

    form_field.input_name('Name')
    form_field.input_password('pass123456')

    form_field.click_drink()

    form_field.click_color()
    time.sleep(1)

    form_field.click_dropdown()
    form_field.click_dropdown_option()

    form_field.input_email('testmail@test.com')
    form_field.input_message('here is message')

    form_field.click_submit()
    # receive success message
    time.sleep(1)

    assert "Message received!" in form_field.get_alert_text()


    time.sleep(1)