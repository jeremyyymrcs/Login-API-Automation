class HomePageLocators:
    WELCOME_LABEL = "//h1[contains(text(),'Welcome!')]"


class LoginPageLocators:
    MFA_LOGIN_TESTING_PAGE_LABEL = "//h4[contains(.,'MFA Login Testing Page')]"
    USERNAME = "//input[@id='username']"
    PASSWORD = "//input[@id='password']"
    MULTIFACTOR_AUTH_CODE = "//input[contains(@placeholder,'Enter the 6-digit MFA Code')]"
    SIGN_IN_BUTTON = "//a[@id='log-in']"
    INVALID_PASSWORD_WARNING = "//h6[contains(.,'Invalid Password!')]"


class SignUpPageLocators:
    TOTP_CODE = "//*[(contains(@id, 'totp'))]"
    SIGN_UP_REDIRECTION = "//a[contains(.,'seleniumbase.io/realworld/signup')]"
    PASSWORD_INPUT = "//input[@id='password']"
