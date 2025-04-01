
class Credentials:
    # examples of credentials
    OWNER = ('test_mail+owner@gmail.com', 'password')
    NO_PROPERTY = ('test_mail+no_property@gmail.com', 'password')
    # for negative scenarios
    NO_PASS = ('email@email.email', '')
    NO_LOGIN = ('', 'password')
    NO_BOTH = ('', '')
    WRONG = ('email@email.email', 'Apassword')

class Urls:

    PROJECT_STAGE = "https://stage.automation-qa-help.com/"
    PROJECT_PROD = "https://automation-qa-help.com/"



