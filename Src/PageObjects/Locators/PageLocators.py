from selenium.webdriver.common.by import By


# LOGIN_PAGE
OrangeHRMLogo = (By.XPATH, "//img[@alt='company-branding']")
LoginTitle = (By.XPATH, "//*[contains(@class,'orangehrm-login-title')]")
AdmUsername = (By.NAME, 'username')
AdmPassword = (By.NAME, 'password')
LoginBtn = (By.XPATH, "//button[@type='submit' and contains(@class,'orangehrm-login-button')]")
ForgotPwd = (By.XPATH, "//*[@class='orangehrm-login-forgot']/p[contains(.,'Forgot your password')]")

# DASHBOARD_PAGE
# TO BE UPDATED
