# Import WebDriverWait for explicit waits
from selenium.webdriver.support.ui import WebDriverWait as W
# Import expected_conditions for explicit waits
from selenium.webdriver.support import expected_conditions as EC

# Import locators from locators module
from .locators import (
    IndexPageLocators, 
    SignupPageLocators, 
    LoginPageLocators, 
    CreatePageLocators, 
    UpdatePageLocators, 
    DeletePageLocators, 
    StrategiesPageLocators, 
    MarketPageLocators )


# Base page class to handle common actions
class BasePage(object):

    # Initialize the BasePage with a WebDriver instance
    def __init__(self, driver):
        self.driver = driver

    # Clear the text field located by locator
    def do_clear(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    # Click the element located by locator
    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    # Submit the form located by locator
    def do_submit(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    # Send keys to the text field located by locator
    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    # Get a single element located by locator
    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    # Get multiple elements located by locator
    def get_elements(self, locator):
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    # Get text of the element located by locator
    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    # Submit the form located by locator 
    def select_value(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()


# Index page class to handle actions specific to the index page
class IndexPage(BasePage):

    # Verify if the page title matches expected value
    def is_title_matches(self):
        return 'Quant Catalog | Home' in self.driver.title

    # Verify if the index heading is displayed correctly
    def is_index_heading_displayed_correctly(self):
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'Hi, I’m Your Trading Mentor'
        return text in index_heading

    # Verify if the signup link works correctly
    def is_signup_link_works(self):
        self.do_click(IndexPageLocators.SIGNUP_LINK)
        return 'Quant Catalog | Signup' in self.driver.title

    # Verify if the logo link works correctly
    def is_logo_link_works(self):
        self.do_click(IndexPageLocators.LOGO_LINK)
        return 'Quant Catalog | Home' in self.driver.title

    # Verify if the login link works correctly
    def is_login_link_works(self):
        self.do_click(IndexPageLocators.LOGIN_LINK)
        return 'Quant Catalog | Login' in self.driver.title

    # Verify if the homepage link works correctly
    def is_homepage_link_works(self):
        self.do_click(IndexPageLocators.HOMEPAGE_LINK)
        return 'Quant Catalog | Home' in self.driver.title

    # Verify if the strategies link works correctly
    def is_strategies_link_works(self):
        self.do_click(IndexPageLocators.STRATEGIES_LINK)
        return 'Quant Catalog | Strategies' in self.driver.title

    # Verify if the markets link works correctly
    def is_markets_link_works(self):
        self.do_click(IndexPageLocators.OPENER_LINK)
        self.do_click(IndexPageLocators.MARKET_LINK)
        return 'Quant Catalog | Stocks' in self.driver.title

    # Verify if the CAGR link works correctly
    def is_cagr_link_works(self):
        self.do_click(IndexPageLocators.CAGR_LINK)
        return 'Quant Catalog | CAGR' in self.driver.title

    # Verify if the Sharpe link works correctly
    def is_sharpe_link_works(self):
        self.do_click(IndexPageLocators.SHARPE_LINK)
        return 'Quant Catalog | Sharpe' in self.driver.title

    # Verify if the Long Only link works correctly
    def is_long_link_works(self):
        self.do_click(IndexPageLocators.LONG_LINK)
        return 'Quant Catalog | Long Only' in self.driver.title

# Signup page class to handle actions specific to the signup page
class SignupPage(BasePage):

    # Verify if the page title matches expected value
    def is_title_matches(self):
        return 'Quant Catalog | Signup' in self.driver.title 

    # Verify if the signup form works correctly
    def is_signup_form_works(self):
        self.do_clear(SignupPageLocators.USERNAME_FIELD)
        self.do_clear(SignupPageLocators.PASSWORD1_FIELD)
        self.do_clear(SignupPageLocators.PASSWORD2_FIELD)
        self.do_send_keys(SignupPageLocators.USERNAME_FIELD, 'mjaroszewski')
        self.do_send_keys(SignupPageLocators.PASSWORD1_FIELD, 'maciej_1245')
        self.do_send_keys(SignupPageLocators.PASSWORD2_FIELD, 'maciej_1245')
        self.do_click(SignupPageLocators.SUBMIT_BUTTON)
        return 'Quant Catalog | Login' in self.driver.title 

# Login page class to handle actions specific to the login page
class LoginPage(BasePage):

    # Verify if the page title matches expected value
    def is_title_matches(self):
        return 'Quant Catalog | Login' in self.driver.title 

    # Verify if the login form works correctly
    def is_login_form_works(self):
        self.do_clear(LoginPageLocators.USERNAME_FIELD)
        self.do_clear(LoginPageLocators.PASSWORD_FIELD)
        self.do_send_keys(LoginPageLocators.USERNAME_FIELD, 'testuser')
        self.do_send_keys(LoginPageLocators.PASSWORD_FIELD, '12345')
        self.do_click(LoginPageLocators.LOGIN_BUTTON)
        logout_text = self.get_element_text(LoginPageLocators.LOGOUT_LINK)
        return 'LOGOUT' in logout_text

    # Verify if the logout link works correctly
    def is_logout_link_works(self):
        self.do_click(LoginPageLocators.LOGOUT_LINK)
        return 'Quant Catalog | Home' in self.driver.title

# Create page class to handle actions specific to the create page
class CreatePage(BasePage):

    # Verify if the page title matches expected value
    def is_title_matches(self):
        return 'Quant Catalog | Create Strategy' in self.driver.title 

    # Verify if the create form works correctly
    def is_create_form_works(self):
        self.do_clear(CreatePageLocators.TITLE_FIELD)
        self.do_clear(CreatePageLocators.SLUG_FIELD)
        self.do_clear(CreatePageLocators.CAGR_FIELD)
        self.do_clear(CreatePageLocators.SHARPE_FIELD)
        self.do_clear(CreatePageLocators.DESCRIPTION_FIELD)
        self.do_send_keys(CreatePageLocators.TITLE_FIELD, 'price_action')
        self.do_send_keys(CreatePageLocators.SLUG_FIELD, 'price_action')
        self.do_send_keys(CreatePageLocators.CAGR_FIELD, 5)
        self.do_send_keys(CreatePageLocators.SHARPE_FIELD, 1)
        self.do_send_keys(CreatePageLocators.DESCRIPTION_FIELD, 'lorem ipsum')
        self.do_click(CreatePageLocators.MARKET_FIELD)
        self.do_click(CreatePageLocators.CREATE_BUTTON)
        create_msg = self.get_element_text(CreatePageLocators.CREATE_MSG)
        return 'Strategy was created successfully' in create_msg

# Update page class to handle actions specific to the update page
class UpdatePage(BasePage):

    # Verify if the page title matches expected value
    def is_title_matches(self):
        return 'Quant Catalog | Update Strategy' in self.driver.title 

    # Verify if the update form works correctly
    def is_update_form_works(self):
        self.do_clear(CreatePageLocators.DESCRIPTION_FIELD)
        self.do_send_keys(CreatePageLocators.DESCRIPTION_FIELD, 'lorem ipsum')
        self.select_value(CreatePageLocators.MARKET_FIELD)
        self.do_click(UpdatePageLocators.UPDATE_BUTTON)
        update_msg = self.get_element_text(UpdatePageLocators.UPDATE_MSG)
        return 'Strategy was updated successfully' in update_msg

# Delete page class to handle actions specific to the delete page
class DeletePage(BasePage):

    # Verify if the delete form works correctly
    def is_delete_form_works(self):
        self.do_clear(LoginPageLocators.USERNAME_FIELD)
        self.do_clear(LoginPageLocators.PASSWORD_FIELD)
        self.do_send_keys(LoginPageLocators.USERNAME_FIELD, 'testuser')
        self.do_send_keys(LoginPageLocators.PASSWORD_FIELD, '12345')
        self.do_click(DeletePageLocators.ADMIN_LOGIN)
        self.do_click(DeletePageLocators.VIEW_SITE_LINK)
        self.do_click(IndexPageLocators.STRATEGIES_LINK)
        self.do_click(DeletePageLocators.DELETE_LINK)
        self.do_click(DeletePageLocators.DELETE_BUTTON)
        delete_msg = self.get_element_text(UpdatePageLocators.UPDATE_MSG)
        return 'Strategy was deleted successfully' in delete_msg

# Strategies page class to handle actions specific to the strategies page
class StrategiesPage(BasePage):

    # Verify if the page title matches expected value
    def is_title_matches(self):
        return 'Quant Catalog | Strategies' in self.driver.title 

    # Verify if the strategies heading is displayed correctly
    def is_strategies_heading_displayed_correctly(self):
        strategies_heading = self.get_element_text(StrategiesPageLocators.STRATEGIES_TITLE)
        text = 'MOMENTUM'
        return text in strategies_heading

# Strategies detail page class to handle actions specific to the strategies detail page
class StrategiesDetailPage(BasePage):

    # Verify if the page title matches expected value
    def is_title_matches(self):
        return 'Quant Catalog | Momentum' in self.driver.title 

    # Verify if the strategies detail heading is displayed correctly
    def is_strategies_detail_heading_displayed_correctly(self):
        strategies_heading = self.get_element_text(StrategiesPageLocators.STRATEGIES_TITLE)
        text = 'DETAILED INFORMATION ABOUT MOMENTUM'
        return text in strategies_heading

# Market detail page class to handle actions specific to the market detail page
class MarketDetailPage(BasePage):

    # Verify if the page title matches expected value
    def is_title_matches(self):
        return 'Quant Catalog | Stocks' in self.driver.title 

    # Verify if the market detail heading is displayed correctly
    def is_market_detail_heading_displayed_correctly(self):
        market_heading = self.get_element_text(MarketPageLocators.MARKET_HEADING)
        text = 'STOCKS - INVESTMENT IDEAS'
        return text in market_heading
