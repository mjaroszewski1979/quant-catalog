# Import the importlib module for dynamic import and reload
import importlib

# Import SuccessMessageMixin for success messages in class-based views
from django.contrib.messages.views import SuccessMessageMixin
# Import reverse for URL reversing
from django.urls import reverse
# Import reverse_lazy for lazy URL reversing
from django.urls import reverse_lazy
# Import render for rendering templates and get_object_or_404 for object retrieval
from django.shortcuts import render, get_object_or_404
# Import Q for complex queries
from django.db.models import Q
# Import View for class-based views
from django.views import View
# Import generic views for CRUD operations
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Import GroupRequiredMixin for group-based permissions
from braces.views import GroupRequiredMixin

# Import Strategy and Market models
from .models import Strategy, Market
# Import StrategyForm and SignUpForm
from .forms import StrategyForm, SignUpForm
# Import utilities module
from . import utilities


# Home view to display the homepage
class HomeView(View):
    
    def get(self, request):
        # Initialize context dictionary
        context = {}
        # Add all strategies to context
        context['strategies'] = Strategy.objects.all()
        # Reload utilities module
        importlib.reload(utilities)
        # Add zipped data from utilities to context
        context['zips'] = utilities.zips
        # Render the index template with context
        return render(request, 'index.html', context)

# View to list all strategies
class StrategiesList(ListView):
    # Define model to be used
    model = Strategy
    # Define template to be used
    template_name = 'strategies_list.html'

# View to handle user sign-up
class SignUpView(CreateView):
    # Define form class to be used
    form_class = SignUpForm
    # Define URL to redirect to on success
    success_url = reverse_lazy('login')
    # Define template to be used
    template_name = 'signup.html'
    # Define success message
    success_message = "New user was created successfully"

# View to create a new strategy
class StrategiesCreate(SuccessMessageMixin, CreateView):
    # Define model to be used
    model = Strategy
    # Define template to be used
    template_name = 'strategies_create.html'
    # Define form class to be used
    form_class = StrategyForm
    # Define URL to redirect to on success
    success_url = '.'
    # Define success message
    success_message = "Strategy was created successfully"

# View to update an existing strategy
class StrategiesUpdate(SuccessMessageMixin, UpdateView):
    # Define model to be used
    model = Strategy
    # Define template to be used
    template_name = 'strategies_update.html'
    # Define form class to be used
    form_class = StrategyForm
    # Define URL to redirect to on success
    success_url = '.'
    # Define success message
    success_message = "Strategy was updated successfully"

# View to delete an existing strategy with group-based permission check
class StrategiesDelete(GroupRequiredMixin, SuccessMessageMixin, DeleteView):
    # Define required group
    group_required = u"quant"
    # Define template to be used
    template_name = 'strategies_delete.html'
    # Define success message
    success_message = "Strategy was deleted successfully"
    
    def get_object(self):
        # Retrieve slug from URL
        self.slug = self.kwargs.get('slug')
        # Retrieve the strategy object based on slug
        return get_object_or_404(Strategy, slug=self.slug)

    def get_success_url(self):
        # Define URL to redirect to on success
        return reverse('strategies_list')

# View to display details of a specific strategy
class StrategiesDetail(DetailView):
    # Define template to be used
    template_name = 'strategies_detail.html'
    
    def get_object(self):
        # Get all strategies
        queryset = Strategy.objects.all()
        # Retrieve slug from URL
        self.slug = self.kwargs.get('slug')
        # Filter strategies based on market title
        self.strats = Strategy.objects.filter(market__title__startswith=self.slug)
        return queryset

    def get_context_data(self, **kwargs):
        # Get context data from base implementation
        context = super().get_context_data(**kwargs)
        # Add filtered strategies to context
        context['strats'] = self.strats
        # Add slug to context
        context['slug'] = self.slug.upper()
        return context

# View to display details of a specific strategy
class StrategyView(DetailView):
    # Define template to be used
    template_name = 'strategy.html'
    
    def get_object(self):
        # Get all strategies
        queryset = Strategy.objects.all()
        # Retrieve slug from URL
        self.slug = self.kwargs.get('slug')
        # Retrieve the strategy object based on slug
        self.strategy = get_object_or_404(Strategy, slug=self.slug)
        # Get all markets related to the strategy
        self.markets = self.strategy.market.all()
        return queryset

    def get_context_data(self, **kwargs):
        # Get context data from base implementation
        context = super().get_context_data(**kwargs)
        # Add strategy to context
        context['strategy'] = self.strategy
        # Add markets to context
        context['markets'] = self.markets
        return context

# View to display details of a specific market
class MarketDetail(DetailView):
    # Define template to be used
    template_name = 'market_detail.html'
    
    def get_object(self):
        # Get all markets
        queryset = Market.objects.all()
        # Retrieve slug from URL
        self.slug = self.kwargs.get('slug')
        # Retrieve the market object based on slug
        self.market = get_object_or_404(Market, slug=self.slug)
        return queryset

    def get_context_data(self, **kwargs):
        # Get context data from base implementation
        context = super().get_context_data(**kwargs)
        # Add market to context
        context['market'] = self.market
        return context

# View to handle search functionality
class SearchView(View):
    # Define template to be used
    template_name = 'search.html'

    def get(self, request):
        # Initialize context dictionary
        context = {}
        # Get search query from request
        query = request.GET.get('query', '')
        # Filter strategies based on query
        strategies = Strategy.objects.filter(Q(title__icontains=query) |  Q(description__icontains=query))
        # Filter markets based on query
        markets = Market.objects.filter(title__icontains=query)
        # Add query to context
        context['query'] = query
        # Add first matching strategy to context
        context['strategy'] = strategies.first()
        # Add first matching market to context
        context['market'] = markets.first()
        # Render the search template with context
        return render(request, 'search.html', context)

# Custom 404 error handler
def page_not_found(response, exception):
    return render(response, '404.html')

# Custom 500 error handler
def server_error(response):
    return render(response, '500.html')




    





