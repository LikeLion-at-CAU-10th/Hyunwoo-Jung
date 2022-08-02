from django.urls import path
from .views import GenericsCreateView, GenericsListView, GenericsDeleteView, GenericsUpdateView, GenericsDetailView

urlpatterns = [
    path('create/', GenericsCreateView.as_view(), name="generics_create"),
    path('list/', GenericsListView.as_view(), name="generics_list_all"),
    path('delete/<int:pk>', GenericsDeleteView.as_view(),name="generics_delete"),
    path('update/<int:pk>', GenericsUpdateView.as_view(), name="generics_update"),
    path('detail/<int:pk>', GenericsDetailView.as_view(), name="generics_detail"),
]