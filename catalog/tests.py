# Import TemplateView for rendering static templates
from django.views.generic.base import TemplateView
# Import LoginView and LogoutView for authentication
from django.contrib.auth.views import LoginView, LogoutView
# Import TestCase and Client for testing
from django.test import TestCase, Client
# Import reverse and resolve for URL resolution
from django.urls import reverse, resolve
# Import User and Group models for authentication and authorization
from django.contrib.auth.models import User, Group

# Import views from the current app
from . import views
# Import Strategy model for testing
from .models import Strategy


class CatalogTest(TestCase):

    def setUp(self):
        """
        Set up the test environment. Create a client, a new strategy, a user group, and a test user.
        """
        
        self.client = Client()
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
        self.user = User.objects.create_user(username='testuser', password='12345')

    def tearDown(self):
        """
        Clean up after each test. Delete the test user and group.
        """
        
        self.user.delete()
        self.group.delete()

    def test_index_url_is_resolved(self):
        """
        Test that the home URL resolves to the correct view.
        """
        
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, views.HomeView)

    def test_index_get(self):
        """
        Test the GET request for the home page. Check the response contains the correct title and template.
        """
        
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'Quant Catalog | Home', status_code=200)
        self.assertTemplateUsed(response, 'index.html')
        strategy = response.context['strategies'][0]
        self.assertEquals(str(strategy), str(self.new_strategy))

    def test_cagr_url_is_resolved(self):
        """
        Test that the CAGR URL resolves to the correct view.
        """
        
        url = reverse('cagr')
        self.assertEquals(resolve(url).func.view_class, TemplateView)

    def test_cagr_get(self):
        """
        Test the GET request for the CAGR page. Check the response contains the correct title and template.
        """
        
        response = self.client.get(reverse('cagr'))
        self.assertContains(response, 'Quant Catalog | CAGR', status_code=200)
        self.assertTemplateUsed(response, 'cagr.html')

    def test_sharpe_url_is_resolved(self):
        """
        Test that the Sharpe URL resolves to the correct view.
        """
        
        url = reverse('sharpe')
        self.assertEquals(resolve(url).func.view_class, TemplateView)

    def test_sharpe_get(self):
        """
        Test the GET request for the Sharpe page. Check the response contains the correct title and template.
        """
        
        response = self.client.get(reverse('sharpe'))
        self.assertContains(response, 'Quant Catalog | Sharpe', status_code=200)
        self.assertTemplateUsed(response, 'sharpe.html')

    def test_long_url_is_resolved(self):
        """
        Test that the Long Only URL resolves to the correct view.
        """

        url = reverse('long')
        self.assertEquals(resolve(url).func.view_class, TemplateView)

    def test_long_get(self):
        """
        Test the GET request for the Long Only page. Check the response contains the correct title and template.
        """
        
        response = self.client.get(reverse('long'))
        self.assertContains(response, 'Quant Catalog | Long Only', status_code=200)
        self.assertTemplateUsed(response, 'long.html')

    def test_search_url_is_resolved(self):
        """
        Test that the Search URL resolves to the correct view.
        """
        
        url = reverse('search')
        self.assertEquals(resolve(url).func.view_class, views.SearchView)

    def test_search_get(self):
        """
        Test the GET request for the Search page. Check the response contains the correct title and template.
        """
        
        response = self.client.get(reverse('search'))
        self.assertContains(response, 'Quant Catalog | Search', status_code=200)
        self.assertTemplateUsed(response, 'search.html')

    def test_search_query(self):
        """
        Test the search functionality with a query. Check that the context contains the correct query and market.
        """
        
        response = self.client.get('/search/?query=stocks')
        query = response.context['query']
        context_strategy = response.context['strategy']
        context_market = response.context['market']
        self.assertEquals(query, 'stocks')
        self.assertEquals(str(context_market), 'stocks')
        self.assertEquals(context_strategy, None)

    def test_signup_url_is_resolved(self):
        """
        Test that the Signup URL resolves to the correct view.
        """
        
        url = reverse('signup')
        self.assertEquals(resolve(url).func.view_class, views.SignUpView)

    def test_signup_get(self):
        """
        Test the GET request for the Signup page. Check the response contains the correct title and template.
        """
        
        response = self.client.get(reverse('signup'))
        self.assertContains(response, 'Quant Catalog | Signup', status_code=200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_post(self):
        """
        Test the POST request for the Signup page. Check that a new user can sign up and is redirected to the login page.
        """
        
        data={
            'username' : 'maciej123',
            'password1' : 'jaroszewski',
            'password2' : 'jaroszewski'
        }
        response = self.client.post(reverse('signup'), data, follow=True)
        self.assertContains(response, 'Quant Catalog | Login', status_code=200)
        self.assertTemplateUsed(response, 'login.html')

    def test_login_url_is_resolved(self):
        """
        Test that the Login URL resolves to the correct view.
        """
        
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_login_get(self):
        """
        Test the GET request for the Login page. Check the response contains the correct title and template.
        """
        
        response = self.client.get(reverse('login'))
        self.assertContains(response, 'Quant Catalog | Login', status_code=200)
        self.assertTemplateUsed(response, 'login.html')

    def test_logout_url_is_resolved(self):
        """
        Test that the Logout URL resolves to the correct view.
        """
        
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_strategies_create_url_is_resolved(self):
        """
        Test that the Create Strategy URL resolves to the correct view.
        """
        
        url = reverse('strategies_create')
        self.assertEquals(resolve(url).func.view_class, views.StrategiesCreate)

    def test_strategies_create_get(self):
        """
        Test the GET request for the Create Strategy page. Check the response contains the correct title and template.
        """
        
        response = self.client.get(reverse('strategies_create'))
        self.assertContains(response, 'Quant Catalog | Create Strategy', status_code=200)
        self.assertTemplateUsed(response, 'strategies_create.html')

    def test_strategies_create_post(self):
        """
        Test the POST request for the Create Strategy page. Check that a new strategy can be created.
        """
        
        data={
            'title' : 'trend_following',
            'slug' : 'trendfollowing',
            'cagr' : 5,
            'sharpe' : 1,
            'market' : 'stocks',
            'long_only' : True,
            'description' : 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'
        }
        response = self.client.post(reverse('strategies_create'), data, follow=True)
        self.assertContains(response, 'Quant Catalog | Create Strategy', status_code=200)
        self.assertTemplateUsed(response, 'strategies_create.html')

    def test_strategies_update_url_is_resolved(self):
        """
        Test that the Update Strategy URL resolves to the correct view.
        """
        
        url = reverse('strategies_update', args= (self.new_strategy.slug, ))
        self.assertEquals(resolve(url).func.view_class, views.StrategiesUpdate)

    def test_strategies_update_get(self):
        """
        Test the GET request for the Update Strategy page. Check the response contains the correct title and template.
        """
        
        response = self.client.get(reverse('strategies_update', args= (self.new_strategy.slug, )))
        self.assertContains(response, 'Quant Catalog | Update Strategy', status_code=200)
        self.assertTemplateUsed(response, 'strategies_update.html')

    def test_strategies_update_post(self):
        """
        Test the POST request for the Update Strategy page. Check that an existing strategy can be updated.
        """
        
        data={
            'title' : 'trend_following',
            'slug' : 'trendfollowing',
            'cagr' : 5,
            'sharpe' : 1,
            'market' : 'stocks',
            'long_only' : True,
            'description' : 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'
        }
        response = self.client.post(reverse('strategies_update', args= (self.new_strategy.slug, )), data, follow=True)
        self.assertContains(response, 'Quant Catalog | Update Strategy', status_code=200)
        self.assertTemplateUsed(response, 'strategies_update.html')

    def test_strategy_detail_url_is_resolved(self):
        """
        Test that the Strategy Detail URL resolves to the correct view.
        """
        
        url = reverse('strategy_detail', args= (self.new_strategy.slug, ))
        self.assertEquals(resolve(url).func.view_class, views.StrategyView)

    def test_strategy_detail_get(self):
        """
        Test the GET request for the Strategy Detail page. Check the response contains the correct title and template.
        """
        
        response = self.client.get(reverse('strategy_detail', args= (self.new_strategy.slug, )))
        self.assertContains(response, 'Quant Catalog | ' + self.new_strategy.title.capitalize(), status_code=200)
        self.assertTemplateUsed(response, 'strategy.html')

    def test_strategies_delete_url_is_resolved(self):
        """
        Test that the Delete Strategy URL resolves to the correct view.
        """
        
        url = reverse('strategies_delete', args= (self.new_strategy.slug, ))
        self.assertEquals(resolve(url).func.view_class, views.StrategiesDelete)

    def test_strategies_delete_user_in_group(self):
        """
        Test the GET request for the Delete Strategy page. Check that a user in the 'quant' group can access the page.
        """
        
        self.group.user_set.add(self.user)
        self.group.save()
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('strategies_delete', args= (self.new_strategy.slug, )), follow=True)
        self.assertContains(response, 'Quant Catalog | Delete Strategy', status_code=200)
        self.assertTemplateUsed(response, 'strategies_delete.html')

    def test_strategies_delete_user_not_in_group(self):
        """
        Test the GET request for the Delete Strategy page. Check that a user not in the 'quant' group is redirected to the login page.
        """
        
        response = self.client.get(reverse('strategies_delete', args= (self.new_strategy.slug, )), follow=True)
        self.assertTemplateUsed(response, 'login.html')

    def test_strategies_delete_post_user_in_group(self):
        """
        Test the POST request for the Delete Strategy page. Check that a strategy can be deleted by a user in the 'quant' group.
        """
        
        self.group.user_set.add(self.user)
        self.group.save()
        self.client.login(username='testuser', password='12345')
        data= {
            'value' : 'Delete'
        }
        response = self.client.post(reverse('strategies_delete', args= (self.new_strategy.slug, )), data, follow=True)
        strategies_count = Strategy.objects.count()
        self.assertTemplateUsed(response, 'strategies_list.html')
        self.assertEquals(strategies_count, 0)


    



    





        
