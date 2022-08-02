from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
# Create your views here.

class LIkeLionCreateView(CreateView):
    model=LIkeLion
    
    
