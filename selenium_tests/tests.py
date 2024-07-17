# Import StaticLiveServerTestCase for live server testing
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# Import Selenium WebDriver
from selenium import webdriver
# Import User and Group models
from django.contrib.auth.models import User, Group
# Import reverse for URL reversing
from django.urls import reverse

# Import page module
from . import page
# Import Strategy and Market models
from catalog.models import Strategy, Market

# Test class for Quant application using StaticLiveServerTestCase
class QuantTest(StaticLiveServerTestCase):

    # Setup method to initialize test data and browser
    def setUp(self):
        # Initialize Chrome WebDriver
        self.driver =  webdriver.Chrome('selenium_tests/chromedriver.exe')
        # Set browser window size
        self.driver.set_window_size(1920, 1080)

        # Create a new Strategy object for testing
        self.new_strategy = Strategy.objects.create(
            title = 'momentum',
            slug = 'momentum',
            cagr = 7,
            sharpe = 1,
            long_only = False,
            description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, qui sed similique doloribus incidunt voluptatem debitis doloremque iure suscipit dignissimos!'
        )
        # Save the new strategy
        self.new_strategy.save()
        # Create and associate a Market object with the strategy
        self.new_strategy.market.create(
            title = 'stocks',
            slug = 'stocks'
        )
        group_name = 'quant'
        self.group = Group(name=group_name)
        self.group.save()
        self.user = User.objects.create(
            username='superuser', password='secret'
        )
        self.user.save()

    # Teardown method to clean up after tests
    def tearDown(self):
        self.user.delete()
        self.group.delete()
        self.driver.close()


    # Test for the index page
    def test_indexpage(self):
        self.driver.get(self.live_server_url)
        index_page = page.IndexPage(self.driver)
        assert index_page.is_title_matches()
        assert index_page.is_index_heading_displayed_correctly()
        assert index_page.is_signup_link_works()
        assert index_page.is_logo_link_works()
        assert index_page.is_login_link_works()
        assert index_page.is_strategies_link_works()
        assert index_page.is_markets_link_works()
        assert index_page.is_cagr_link_works()
        assert index_page.is_sharpe_link_works()

    # Test for the signup page
    def test_signuppage(self):
        self.driver.get(self.live_server_url + reverse('signup'))
        signup_page = page.SignupPage(self.driver)
        assert signup_page.is_title_matches()
        assert signup_page.is_signup_form_works()

    # Test for the login page
    def test_loginpage(self):
        self.driver.get(self.live_server_url + reverse('login'))
        login_page = page.LoginPage(self.driver)
        assert login_page.is_title_matches()
        assert login_page.is_login_form_works()
        assert login_page.is_logout_link_works()

    # Test for the create strategy page
    def test_createpage(self):
        self.driver.get(self.live_server_url + reverse('strategies_create'))
        create_page = page.CreatePage(self.driver)
        assert create_page.is_title_matches()
        assert create_page.is_create_form_works()

    # Test for the update strategy page
    def test_updatepage(self):
        self.group.user_set.add(self.user)
        self.group.save()
        self.client.login(username='testuser', password='12345')
        self.driver.get(self.live_server_url + reverse('strategies_update', args= (self.new_strategy.slug, )))
        update_page = page.UpdatePage(self.driver)
        assert update_page.is_title_matches()
        assert update_page.is_update_form_works()

    # Test for the strategies list page
    def test_strategiespage(self):
        self.driver.get(self.live_server_url + reverse('strategies_list'))
        strategies_page = page.StrategiesPage(self.driver)
        assert strategies_page.is_title_matches()
        assert strategies_page.is_strategies_heading_displayed_correctly()

    # Test for the delete strategy page
    def test_deletepage(self):
        self.group.user_set.add(self.user)
        self.group.save()
        self.driver.get(self.live_server_url + '/admin/')
        delete_page = page.DeletePage(self.driver)
        assert delete_page.is_delete_form_works()

    # Test for the strategy detail page
    def test_strategiesdetailpage(self):
        self.driver.get(self.live_server_url + reverse('strategy_detail', args= (self.new_strategy.slug, )))
        strategies_page = page.StrategiesDetailPage(self.driver)
        assert strategies_page.is_title_matches()
        assert strategies_page.is_strategies_detail_heading_displayed_correctly()

    # Test for the market detail page
    def test_marketpage(self):
        market = Market.objects.get(pk=1)
        self.driver.get(self.live_server_url + reverse('market_detail', args= (market.slug, )))
        market_page = page.MarketDetailPage(self.driver)
        assert market_page.is_title_matches()
        assert market_page.is_market_detail_heading_displayed_correctly()





