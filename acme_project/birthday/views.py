from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import BirthdayForm
from .models import Birthday
from .utils import calculate_birthday_countdown


class BirthdayListView(LoginRequiredMixin, ListView):
    model = Birthday
    ordering = 'id'
    paginate_by = 10


class BirthdayCreateView(LoginRequiredMixin, CreateView):
    model = Birthday
    form_class = BirthdayForm
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class BirthdayUpdateView(LoginRequiredMixin, UpdateView):
    model = Birthday
    form_class = BirthdayForm


class BirthdayDeleteView(LoginRequiredMixin, DeleteView):
    model = Birthday
    success_url = reverse_lazy('birthday:list')


class BirthdayDetailView(LoginRequiredMixin, DetailView):
    model = Birthday

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['birthday_countdown'] = calculate_birthday_countdown(
            self.object.birthday
        )
        return context 