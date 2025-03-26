import time

from automation_testing.pom.pages.default_page_example import DefaultPage
from automation_testing.pom.pages.page_example import ExamplePage
from automation_testing.pom.api_setup.setup_before_tests import SetupBeforeTest

# here I setup all needed data
def test_setup_the_system():
    setup = SetupBeforeTest()
    setup.get_sign_up_acc_id('')
    setup.get_all_widget_ids()

# process of test writing is pretty simple
def test_example(login_as_admin_example):
    default = DefaultPage(login_as_admin_example)
    example = ExamplePage(login_as_admin_example)

    time.sleep(0.5)
    default.resfresh()
    time.sleep(0.3)
    # as far as products are not perfect testers always see that smth crashes
    # for that I had to keep it in mind and use 'try catch' structure
    try:
        example.input_example('xxxxxxxxxxxxx')
        time.sleep(0.3)
        default.close_tab()
    except:
        print('exception')
        pass

    time.sleep(0.3)
    default.click_esc()
    example.clear_example_1()

    try:
        default.resfresh()
        for i in range(1, 10):
            example.click_example()
            example.click_example()
        example.click_example()
    except:
        print("xxxxxxxxxxxxx")

    example.click_example()

    example.input_example('1111')
    example.click_example()
    # asserts is main tools to confirm test succeeds
    assert "xxxxxxxxxxxxxxx" in example.get_text_example()
    time.sleep(0.3)

    default.open_new_tab_example()
    default.switch_to_second_window()
    default.switch_to_first_window()

    time.sleep(3)


# here I clear system from generated data
def test_clear_the_system():
    setup = SetupBeforeTest()
    setup_id = setup.get_property_id('my property')
    setup.delete_property(setup_id)
