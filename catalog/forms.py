# Import forms module from Django for creating form classes
from django import forms
# Import User model from Django's authentication system
from django.contrib.auth.models import User
# Import UserCreationForm for user registration forms
from django.contrib.auth.forms import UserCreationForm

# Import the Strategy model from the current module
from .models import Strategy
 
 
class StrategyForm(forms.ModelForm):
    """
    Form class for creating or updating Strategy instances.
    Inherits from Django's ModelForm to automatically handle form field generation based on the Strategy model.
    """
 
    class Meta:

        # Specifies the model associated with this form
        model = Strategy
        fields = [
            "title",
            'slug',
            "market",
            'cagr',
            'sharpe',
            'long_only',
            'description']

class SignUpForm(UserCreationForm):
    """
    Form class for user registration.
    Inherits from Django's UserCreationForm to handle user creation with username and password fields.
    """

    class Meta:
     
        # Specifies the User model associated with this form
        model = User
        fields = [
            'username', 
            'password1', 
            'password2', 
            ]
