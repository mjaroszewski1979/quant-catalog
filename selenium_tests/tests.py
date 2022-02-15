from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from . import page
from catalog.models import Strategy, Market
from django.contrib.auth.models import User, Group
from django.urls import reverse




class BitcoinTest(StaticLiveServerTestCase):

    def setUp(self):
        self.driver =  webdriver.Chrome('selenium_tests/chromedriver.exe')
        self.driver.set_window_size(1920, 1080)
        
        self.new_strategy = Strategy.objects.create(
            title = 'momentum',
            slug = 'momentum',
            cagr = 7,
            sharpe = 1,
            long_only = False,
            description = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Et, qui sed similique doloribus incidunt voluptatem debitis doloremque iure suscipit dignissimos!'
        )
        self.new_strategy.save()
        self.new_strategy.market.create(
            title = 'stocks',
            slug = 'stocks'
        )
        group_name = 'quant'
        self.group = Group(name=group_name)
        self.group.save()
        self.user = User.objects.create_superuser(
            username='superuser', password='secret', email='admin@example.com'
        )
        self.user.force_login(username='superuser', password='secret')

    def tearDown(self):
        self.user.delete()
        self.group.delete()
        self.driver.close()


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

    def test_signuppage(self):
        self.driver.get(self.live_server_url + reverse('signup'))
        signup_page = page.SignupPage(self.driver)
        assert signup_page.is_title_matches()
        assert signup_page.is_signup_form_works()

    def test_loginpage(self):
        self.driver.get(self.live_server_url + reverse('login'))
        login_page = page.LoginPage(self.driver)
        assert login_page.is_title_matches()
        assert login_page.is_login_form_works()
        assert login_page.is_logout_link_works()

    def test_createpage(self):
        self.driver.get(self.live_server_url + reverse('strategies_create'))
        create_page = page.CreatePage(self.driver)
        assert create_page.is_title_matches()
        assert create_page.is_create_form_works()

    def test_updatepage(self):
        self.group.user_set.add(self.user)
        self.group.save()
        self.client.login(username='testuser', password='12345')
        self.driver.get(self.live_server_url + reverse('strategies_update', args= (self.new_strategy.slug, )))
        update_page = page.UpdatePage(self.driver)
        assert update_page.is_title_matches()
        assert update_page.is_update_form_works()

    def test_strategiespage(self):
        self.driver.get(self.live_server_url + reverse('strategies_list'))
        strategies_page = page.StrategiesPage(self.driver)
        assert strategies_page.is_title_matches()
        assert strategies_page.is_strategies_heading_displayed_correctly()

    def test_deletepage(self):
        self.group.user_set.add(self.user)
        self.group.save()
        self.driver.get(self.live_server_url + '/admin/')
        delete_page = page.DeletePage(self.driver)
        assert delete_page.is_delete_form_works()

    def test_strategiesdetailpage(self):
        self.driver.get(self.live_server_url + reverse('strategy_detail', args= (self.new_strategy.slug, )))
        strategies_page = page.StrategiesDetailPage(self.driver)
        assert strategies_page.is_title_matches()
        assert strategies_page.is_strategies_detail_heading_displayed_correctly()

    def test_marketpage(self):
        market = Market.objects.get(pk=1)
        self.driver.get(self.live_server_url + reverse('market_detail', args= (market.slug, )))
        market_page = page.MarketDetailPage(self.driver)
        assert market_page.is_title_matches()
        assert market_page.is_market_detail_heading_displayed_correctly()





