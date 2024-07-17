# Import By class for locating elements
from selenium.webdriver.common.by import By

# Locators for elements on the Index Page
class IndexPageLocators(object):

    # Locator for the main heading on the index page
    INDEX_HEADING = (By.XPATH, "//section[@id='banner']//div[@class='content']//header//h1")
    # Locator for the toggle button in the sidebar
    TOGGLE_BUTTON = (By.XPATH, "//div[@id='sidebar']//div[@class='inner']//a[@class='toggle']")
    # Locator for the signup link
    SIGNUP_LINK = (By.LINK_TEXT, 'SIGNUP')
    # Locator for the logo link
    LOGO_LINK = (By.XPATH, "//header[@id='header']//a[@class='logo']")
    # Locator for the login link
    LOGIN_LINK = (By.LINK_TEXT, 'LOGIN')
    # Locator for the homepage link
    HOMEPAGE_LINK = (By.LINK_TEXT, 'HOMEPAGE')
    # Locator for the strategies link
    STRATEGIES_LINK = (By.LINK_TEXT, 'STRATEGIES')
    # Locator for the opener link in the menu
    OPENER_LINK = (By.XPATH, "//nav[@id='menu']//span[@class='opener']")
    # Locator for the stocks market link
    MARKET_LINK = (By.LINK_TEXT, 'STOCKS')
    # Locator for the CAGR link
    CAGR_LINK = (By.LINK_TEXT, 'CAGR')
    # Locator for the Sharpe Ratio link
    SHARPE_LINK = (By.LINK_TEXT, 'Sharpe Ratio')
    # Locator for the Long Only link
    LONG_LINK = (By.LINK_TEXT, 'Long Only')

# Locators for elements on the Signup Page
class SignupPageLocators(object):

    # Locator for the username field
    USERNAME_FIELD = (By.NAME, 'username')
    # Locator for the first password field
    PASSWORD1_FIELD = (By.NAME, 'password1')
    # Locator for the second password field
    PASSWORD2_FIELD = (By.NAME, 'password2')
    # Locator for the submit button
    SUBMIT_BUTTON = (By.XPATH, "//div[@class='col-12']//input[@class='primary']")

# Locators for elements on the Login Page
class LoginPageLocators(object):

    # Locator for the username field
    USERNAME_FIELD = (By.NAME, 'username')
    # Locator for the first password field
    PASSWORD_FIELD = (By.NAME, 'password')
    # Locator for the login button
    LOGIN_BUTTON = (By.XPATH, "//div[@class='col-12']//input[@class='primary']")
    # Locator for the logout link
    LOGOUT_LINK = (By.LINK_TEXT, 'LOGOUT')

# Locators for elements on the Create Page
class CreatePageLocators(object):

    # Locator for the title field
    TITLE_FIELD = (By.NAME, 'title')
    # Locator for the slug field
    SLUG_FIELD = (By.NAME, 'slug')
    # Locator for the market field
    MARKET_FIELD = (By.ID, 'id_market')
    # Locator for the cagr field
    CAGR_FIELD = (By.NAME, 'cagr')
    # Locator for the sharpe field
    SHARPE_FIELD = (By.NAME, 'sharpe')
    # Locator for the description field
    DESCRIPTION_FIELD = (By.NAME, 'description')
    # Locator for the create button
    CREATE_BUTTON = (By.XPATH, "//div[@class='col-12']//input[@class='primary']")
    # Locator for the create success message
    CREATE_MSG = (By.XPATH, "//div[@class='row']//h2")

# Locators for elements on the Update Page
class UpdatePageLocators(object):

    # Locator for the update button
    UPDATE_BUTTON = (By.XPATH, "//div[@class='col-12']//input[@class='primary']")
    # Locator for the update success message
    UPDATE_MSG = (By.XPATH, "//div[@class='row']//h2")

# Locators for elements on the Delete Page
class DeletePageLocators(object):
    
    # Locator for the delete button
    DELETE_BUTTON = (By.XPATH, "//div[@class='col-12']//input[@class='primary']")
    # Locator for the admin login button
    ADMIN_LOGIN = (By.CLASS_NAME, 'submit-row')
    # Locator for the view site link
    VIEW_SITE_LINK = (By.LINK_TEXT, 'VIEW SITE')
    # Locator for the delete strategy link
    # Locator for the delete strategy link
    DELETE_LINK = (By.LINK_TEXT, 'DELETE STRATEGY')

# Locators for elements on the Strategies Page
class StrategiesPageLocators(object):

    # Locator for the strategies title
    STRATEGIES_TITLE = (By.XPATH, "//section//h1")

# Locators for elements on the Market Page
class MarketPageLocators(object):

    # Locator for the market heading
    MARKET_HEADING = (By.XPATH, "//section//h2")


    









