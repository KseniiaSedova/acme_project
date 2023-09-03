from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegistration(CreateView):
    model = User 
    template_name = 'registration/registration_form.html'
    form_class = CustomUserCreationForm 
    success_url = reverse_lazy('pages:homepage')

