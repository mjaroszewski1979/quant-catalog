# Import path for URL routing
from django.urls import path
# Import auth_views for authentication views
from django.contrib.auth import views as auth_views
# Import TemplateView for static template rendering
from django.views.generic.base import TemplateView

# Import views from the current app
from . import views


urlpatterns = [

    # URL pattern for the search view
    path('search/', views.SearchView.as_view(), name='search'),
 
    # URL pattern for the home view
    path('', views.HomeView.as_view(), name='home'),
 
    # URL pattern for the long-only view
    path('long/', TemplateView.as_view(template_name='long.html'), name='long'),
 
    # URL pattern for the Sharpe ratio view
    path('sharpe/', TemplateView.as_view(template_name='sharpe.html'), name='sharpe'),

    # URL pattern for the CAGR view
    path('cagr/', TemplateView.as_view(template_name='cagr.html'), name='cagr'),

    # URL pattern for creating a new strategy
    path('strategies_create/', views.StrategiesCreate.as_view(), name='strategies_create'),

    # URL pattern for updating an existing strategy
    path('strategies_update/<slug:slug>/', views.StrategiesUpdate.as_view(), name='strategies_update'),

    # URL pattern for deleting an existing strategy
    path('strategies_delete/<slug:slug>/', views.StrategiesDelete.as_view(), name='strategies_delete'),

    # URL pattern for listing all strategies
    path('strategies_list/', views.StrategiesList.as_view(), name='strategies_list'),

    # URL pattern for detailed view of a specific strategy
    path('strategies_list/<slug:slug>/', views.StrategiesDetail.as_view(), name='strategies_detail'),

    # URL pattern for detailed view of a specific strategy
    path('strategy_detail/<slug:slug>/', views.StrategyView.as_view(), name='strategy_detail'),

    # URL pattern for detailed view of a specific market
    path('market_detail/<slug:slug>/', views.MarketDetail.as_view(), name='market_detail'),

    # URL pattern for logging out
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # URL pattern for logging in
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # URL pattern for signing up
    path('signup/', views.SignUpView.as_view(), name='signup'),
 
]

'''
Custom error handlers
'''

# Handler for 404 errors (page not found)
handler404 ='catalog.views.page_not_found'
# Handler for 500 errors (server error)
handler500 ='catalog.views.server_error'
