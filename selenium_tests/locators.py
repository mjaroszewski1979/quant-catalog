from selenium.webdriver.common.by import By

class IndexPageLocators(object):
    
    INDEX_HEADING = (By.XPATH, "//section[@id='banner']//div[@class='content']//header//h1")
    TOGGLE_BUTTON = (By.XPATH, "//div[@id='sidebar']//div[@class='inner']//a[@class='toggle']")
    SIGNUP_LINK = (By.LINK_TEXT, 'SIGNUP')
    LOGO_LINK = (By.XPATH, "//header[@id='header']//a[@class='logo']")
    LOGIN_LINK = (By.LINK_TEXT, 'LOGIN')
    HOMEPAGE_LINK = (By.LINK_TEXT, 'HOMEPAGE')
    STRATEGIES_LINK = (By.LINK_TEXT, 'STRATEGIES')
    OPENER_LINK = (By.XPATH, "//nav[@id='menu']//span[@class='opener']")
    MARKET_LINK = (By.LINK_TEXT, 'STOCKS')
    CAGR_LINK = (By.LINK_TEXT, 'CAGR')
    SHARPE_LINK = (By.LINK_TEXT, 'Sharpe Ratio')
    LONG_LINK = (By.LINK_TEXT, 'Long Only')

class SignupPageLocators(object):

    USERNAME_FIELD = (By.NAME, 'username')
    PASSWORD1_FIELD = (By.NAME, 'password1')
    PASSWORD2_FIELD = (By.NAME, 'password2')
    SUBMIT_BUTTON = (By.XPATH, "//div[@class='col-12']//input[@class='primary']")

class LoginPageLocators(object):

    USERNAME_FIELD = (By.NAME, 'username')
    PASSWORD_FIELD = (By.NAME, 'password')
    LOGIN_BUTTON = (By.XPATH, "//div[@class='col-12']//input[@class='primary']")
    LOGOUT_LINK = (By.LINK_TEXT, 'LOGOUT')

class CreatePageLocators(object):

    TITLE_FIELD = (By.NAME, 'title')
    SLUG_FIELD = (By.NAME, 'slug')
    MARKET_FIELD = (By.ID, 'id_market')
    CAGR_FIELD = (By.NAME, 'cagr')
    SHARPE_FIELD = (By.NAME, 'sharpe')
    DESCRIPTION_FIELD = (By.NAME, 'description')
    CREATE_BUTTON = (By.XPATH, "//div[@class='col-12']//input[@class='primary']")
    CREATE_MSG = (By.XPATH, "//div[@class='row']//h2")

class UpdatePageLocators(object):

    UPDATE_BUTTON = (By.XPATH, "//div[@class='col-12']//input[@class='primary']")
    UPDATE_MSG = (By.XPATH, "//div[@class='row']//h2")

class DeletePageLocators(object):

    DELETE_BUTTON = (By.XPATH, "//div[@class='col-12']//input[@class='primary']")
    ADMIN_LOGIN = (By.CLASS_NAME, 'submit-row')
    VIEW_SITE_LINK = (By.LINK_TEXT, 'VIEW SITE')
    DELETE_LINK = (By.LINK_TEXT, 'DELETE STRATEGY')

class StrategiesPageLocators(object):

    STRATEGIES_TITLE = (By.XPATH, "//section//h1")

class MarketPageLocators(object):

    MARKET_HEADING = (By.XPATH, "//section//h2")


    









