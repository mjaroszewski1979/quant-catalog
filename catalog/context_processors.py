# Import Market and Strategy models from the current module
from .models import Market, Strategy

def menu_markets(request):
    """
    Retrieve all Market objects from the database and prepare them for use in templates.
    Args:
        request: The HTTP request object.
    Returns:
        dict: A dictionary containing all Market objects under the key 'menu_markets'.
    """
    
    markets = Market.objects.all()

    return {'menu_markets': markets}

def menu_strategies(request):
    """
    Retrieve all Strategy objects from the database and prepare them for use in templates.
    Args:
        request: The HTTP request object.
    Returns:
        dict: A dictionary containing all Strategy objects under the key 'menu_strategies'.
    """
    
    strategies = Strategy.objects.all()

    return {'menu_strategies': strategies}
