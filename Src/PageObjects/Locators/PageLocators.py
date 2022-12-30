from selenium.webdriver.common.by import By

# HOME_PAGE
HomeLink = (By.LINK_TEXT, 'Home')
SignInLink = (By.LINK_TEXT, 'Sign In')
SignInLink_2 = (By.LINK_TEXT, 'Sign In to Your Account')

# LOGIN_PAGE
CrateAccountLink = (By.LINK_TEXT, 'Create one now')

# CREATE_ACCOUNT_PAGE
Username = (By.NAME, 'users.loginUserId')
Password = (By.NAME, 'users.password')
PasswordVerify = (By.NAME, 'passwordVerify')
Email = (By.NAME, 'users.userEmail')
EmailVerify = (By.NAME, 'emailVerify')
NotificationPref = (By.XPATH, '//label[@class="chkbox-left" and @for="goPaperLessId"]')
TermsAndConditions = (By.XPATH, '//label[@class="chkbox-left" and @for="userAcceptanceAgreement"]')
CreateAccountBtn = (By.ID, 'indSubmitId')