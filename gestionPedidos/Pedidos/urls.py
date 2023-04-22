from django.urls import path
from . import views
from .views import ComponentListView, ComponentCreateView, ComponentUpdateView, ComponentDeleteView, ComponentDetailView
from .views import ClientListView, ClientCreateView, ClientUpdateView, ClientDeleteView, ClientDetailView
from .views import OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView, OrderDetailView
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductDetailView

urlpatterns = [

    path('', ComponentListView.as_view(), name='component-list'),
    path('new/', ComponentCreateView.as_view(), name='component-create'),
    path('<int:pk>/', ComponentDetailView.as_view(), name='component-detail'),
    path('<int:pk>/update/', ComponentUpdateView.as_view(), name='component-update'),
    path('<int:pk>/delete/', ComponentDeleteView.as_view(), name='component-delete'),
    
]

urlpatterns = [
    path('', ClientListView.as_view(), name='client-list'),
    path('new/', ClientCreateView.as_view(), name='client-create'),
    path('<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
]


urlpatterns = [
    path('', OrderListView.as_view(), name='order-list'),
    path('new/', OrderCreateView.as_view(), name='order-create'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('<int:pk>/update/', OrderUpdateView.as_view(), name='order-update'),
    path('<int:pk>/delete/', OrderDeleteView.as_view(), name='client-delete'),
    ]

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('new/', ProductCreateView.as_view(), name='product-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
]



