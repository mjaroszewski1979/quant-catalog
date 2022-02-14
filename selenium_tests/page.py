from selenium.webdriver.support.ui import WebDriverWait as W
from selenium.webdriver.support import expected_conditions as EC
from .locators import IndexPageLocators, SignupPageLocators, LoginPageLocators, CreatePageLocators, UpdatePageLocators, DeletePageLocators, StrategiesPageLocators




class BasePage(object):


    def __init__(self, driver):
        self.driver = driver

    def do_clear(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()

    def do_click(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).click()

    def do_submit(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()

    def do_send_keys(self, locator, text):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_element(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element

    def get_elements(self, locator):
        elements = W(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def get_element_text(self, locator):
        element = W(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return element.text

    def select_value(self, locator):
        W(self.driver, 10).until(EC.visibility_of_element_located(locator)).submit()




    


class IndexPage(BasePage):

    def is_title_matches(self):
        return 'Quant Catalog | Home' in self.driver.title

    def is_index_heading_displayed_correctly(self):
        index_heading = self.get_element_text(IndexPageLocators.INDEX_HEADING)
        text = 'Hi, I’m Your Trading Mentor'
        return text in index_heading

    def is_signup_link_works(self):
        self.do_click(IndexPageLocators.SIGNUP_LINK)
        return 'Quant Catalog | Signup' in self.driver.title

    def is_logo_link_works(self):
        self.do_click(IndexPageLocators.LOGO_LINK)
        return 'Quant Catalog | Home' in self.driver.title

    def is_login_link_works(self):
        self.do_click(IndexPageLocators.LOGIN_LINK)
        return 'Quant Catalog | Login' in self.driver.title

    def is_homepage_link_works(self):
        self.do_click(IndexPageLocators.HOMEPAGE_LINK)
        return 'Quant Catalog | Home' in self.driver.title

    def is_strategies_link_works(self):
        self.do_click(IndexPageLocators.STRATEGIES_LINK)
        return 'Quant Catalog | Strategies' in self.driver.title

    def is_markets_link_works(self):
        self.do_click(IndexPageLocators.OPENER_LINK)
        self.do_click(IndexPageLocators.MARKET_LINK)
        return 'Quant Catalog | Stocks' in self.driver.title

    def is_cagr_link_works(self):
        self.do_click(IndexPageLocators.CAGR_LINK)
        return 'Quant Catalog | CAGR' in self.driver.title

    def is_sharpe_link_works(self):
        self.do_click(IndexPageLocators.SHARPE_LINK)
        return 'Quant Catalog | Sharpe' in self.driver.title

    def is_long_link_works(self):
        self.do_click(IndexPageLocators.LONG_LINK)
        return 'Quant Catalog | Long Only' in self.driver.title

class SignupPage(BasePage):

    def is_title_matches(self):
        return 'Quant Catalog | Signup' in self.driver.title 

    def is_signup_form_works(self):
        self.do_clear(SignupPageLocators.USERNAME_FIELD)
        self.do_clear(SignupPageLocators.PASSWORD1_FIELD)
        self.do_clear(SignupPageLocators.PASSWORD2_FIELD)
        self.do_send_keys(SignupPageLocators.USERNAME_FIELD, 'mjaroszewski')
        self.do_send_keys(SignupPageLocators.PASSWORD1_FIELD, 'maciej_1245')
        self.do_send_keys(SignupPageLocators.PASSWORD2_FIELD, 'maciej_1245')
        self.do_click(SignupPageLocators.SUBMIT_BUTTON)
        return 'Quant Catalog | Login' in self.driver.title 

class LoginPage(BasePage):

    def is_title_matches(self):
        return 'Quant Catalog | Login' in self.driver.title 

    def is_login_form_works(self):
        self.do_clear(LoginPageLocators.USERNAME_FIELD)
        self.do_clear(LoginPageLocators.PASSWORD_FIELD)
        self.do_send_keys(LoginPageLocators.USERNAME_FIELD, 'testuser')
        self.do_send_keys(LoginPageLocators.PASSWORD_FIELD, '12345')
        self.do_click(LoginPageLocators.LOGIN_BUTTON)
        logout_text = self.get_element_text(LoginPageLocators.LOGOUT_LINK)
        return 'LOGOUT' in logout_text

    def is_logout_link_works(self):
        self.do_click(LoginPageLocators.LOGOUT_LINK)
        return 'Quant Catalog | Home' in self.driver.title

class CreatePage(BasePage):

    def is_title_matches(self):
        return 'Quant Catalog | Create Strategy' in self.driver.title 

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

class UpdatePage(BasePage):

    def is_title_matches(self):
        return 'Quant Catalog | Update Strategy' in self.driver.title 

    def is_update_form_works(self):
        self.do_clear(CreatePageLocators.DESCRIPTION_FIELD)
        self.do_send_keys(CreatePageLocators.DESCRIPTION_FIELD, 'lorem ipsum')
        self.select_value(CreatePageLocators.MARKET_FIELD)
        self.do_click(UpdatePageLocators.UPDATE_BUTTON)
        update_msg = self.get_element_text(UpdatePageLocators.UPDATE_MSG)
        return 'Strategy was updated successfully' in update_msg

class DeletePage(BasePage):

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

class StrategiesPage(BasePage):

    def is_title_matches(self):
        return 'Quant Catalog | Strategies' in self.driver.title 

    def is_strategies_heading_displayed_correctly(self):
        strategies_heading = self.get_element_text(StrategiesPageLocators.STRATEGIES_TITLE)
        text = 'MOMENTUM'
        return text in strategies_heading

class StrategiesDetailPage(BasePage):

    def is_title_matches(self):
        return 'Quant Catalog | Momentum' in self.driver.title 

    def is_strategies_detail_heading_displayed_correctly(self):
        strategies_heading = self.get_element_text(StrategiesPageLocators.STRATEGIES_TITLE)
        text = 'MOMENTUM'
        return text in strategies_heading

class MarketDetailPage(BasePage):

    def is_title_matches(self):
        return 'Quant Catalog | Stocks' in self.driver.title 

    def is_market_detail_heading_displayed_correctly(self):
        market_heading = self.get_element_text(StrategiesPageLocators.STRATEGIES_TITLE)
        text = 'STOCKS - INVESTMENT IDEAS'
        return text in market_heading






    

    