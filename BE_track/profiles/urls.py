from django.urls import path
from .views import *

urlpatterns = [
    path('create-profile/', create_profile, name='create-profile'),
    path('get-profile-all/', get_profile_all, name='get-profile-all'),
    path('create-content/<int:profile_id>', create_content, name='create-content'),
    path('get-content-all/<int:profile_id>', get_content_all, name='get-content-all'),
    
]