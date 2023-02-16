from selenium.webdriver.common.by import By


# LOGIN_PAGE
OrangeHRMLogo = (By.XPATH, "//img[@alt='company-branding']")
LoginTitle = (By.XPATH, "//*[contains(@class,'orangehrm-login-title')]")
AdmUsername = (By.NAME, 'username')
AdmPassword = (By.NAME, 'password')
LoginBtn = (By.XPATH, "//button[@type='submit' and contains(@class,'orangehrm-login-button')]")
ForgotPwd = (By.XPATH, "//*[@class='orangehrm-login-forgot']/p[contains(.,'Forgot your password')]")

# RESET_PASSWORD_PAGE
Username = (By.NAME, 'username')
ResetBtn = (By.XPATH, "//button[@type='submit' and contains(@class,'orangehrm-forgot-password-button--reset')]")
resetPwdSuccessText = (By.XPATH, "//*[contains(@class,'orangehrm-forgot-password-title')]")

# DASHBOARD_PAGE
AdminModule = (By.XPATH, "//a[contains(@href,'viewAdminModule')]")
AdminTopbarHeader = (By.XPATH, "//span[@class='oxd-topbar-header-breadcrumb']")
AddBtn = (By.XPATH, "//button[contains(@class,'oxd-button') and contains(.,'Add')]")

# ADDUSER_PAGE
UserRole = (By.XPATH, "")
EmployeeName = (By.XPATH, "//div[contains(@class,'oxd-autocomplete-text-input')]/input")
EmployeeNameSuggestions = (By.XPATH, "//div[@role='listbox']/div[@role='option']/span")
Status = (By.XPATH, "")
EmpUsername = (By.XPATH, "//label[contains(.,'Username')]/parent::div/following-sibling::div/input")
Password = (By.XPATH, "(//label[contains(text(),'Password')]/parent::div/following-sibling::div/input)[1]")
ConfirmPassword = (By.XPATH, "(//label[contains(text(),'Password')]/parent::div/following-sibling::div/input)[2]")
SaveBtn = (By.XPATH, "//button[@type='submit' and contains(.,'Save')]")
