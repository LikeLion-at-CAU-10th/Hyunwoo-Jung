from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Generics

# Create your views here.
class GenericsCreateView(CreateView):
    model = Generics
    fields = "__all__"
    #fields = ['name',]
    success_url = "/generics"

class GenericsListView(ListView):
    model = Generics
    paginate_by = 30
    ordering = ['-name'] # - 붙이면 역순

class GenericsUpdateView(UpdateView):
    model = Generics
    fields = "__all__"
    template_name_suffix = '_update_form'
    success_url = "/generics"

class GenericsDeleteView(DeleteView):
    model = Generics
    success_url = "/generics"

class GenericsDetailView(DetailView):
    model = Generics
    template_name_suffix = '_detail_form'
    success_url = "/generics"