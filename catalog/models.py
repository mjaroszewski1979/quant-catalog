# Import models module from Django for creating database models
from django.db import models


class Market(models.Model):
    """
    Model class for representing a financial market.
    """

    # Field for the market's title, must be unique and not null or blank
    title = models.CharField(max_length = 200, unique=True, null=False, blank=False)
    # Field for the market's slug
    slug = models.SlugField(max_length = 200)

    class Meta:
        # Singular name for the model in the admin interface
        verbose_name = 'market'
        # Plural name for the model in the admin interface
        verbose_name_plural = 'markets'

    def __str__(self):
        """
        String representation of the Market model.
        Returns the title of the market.
        """
        
        return self.title

class Strategy(models.Model):
    """
    Model class for representing a trading strategy.
    """

    # Field for the strategy's title, must be unique and not null or blank
    title = models.CharField(max_length = 200, unique=True, null=False, blank=False)
    # Field for the strategy's slug, must be unique and not null or blank
    slug = models.SlugField(max_length = 200, unique=True, null=False, blank=False)
    # Many-to-many relationship with the Market model
    market = models.ManyToManyField(Market)
    # Field for the strategy's Compound Annual Growth Rate
    cagr = models.DecimalField(max_digits=3, decimal_places=2)
    # Field for the strategy's Sharpe ratio
    sharpe = models.DecimalField(max_digits=3, decimal_places=2)
    # Field indicating if the strategy is long-only
    long_only = models.BooleanField(default=True)
    # Field for the strategy's description
    description = models.TextField()

    class Meta:
        # Singular name for the model in the admin interface
        verbose_name = 'strategy'
        # Plural name for the model in the admin interface
        verbose_name_plural = 'strategies'

    def __str__(self):
        """
        String representation of the Strategy model.
        Returns the title of the strategy.
        """
        
        return self.title





