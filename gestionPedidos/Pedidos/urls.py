from django.urls import path
from . import views
from .views import ComponentListView, ComponentCreateView, ComponentUpdateView, ComponentDeleteView, ComponentDetailView

urlpatterns = [

    path('', ComponentListView.as_view(), name='component-list'),
    path('new/', ComponentCreateView.as_view(), name='component-create'),
    path('<int:pk>/', ComponentDetailView.as_view(), name='component-detail'),
    path('<int:pk>/update/', ComponentUpdateView.as_view(), name='component-update'),
    path('<int:pk>/delete/', ComponentDeleteView.as_view(), name='component-delete'),
    
]