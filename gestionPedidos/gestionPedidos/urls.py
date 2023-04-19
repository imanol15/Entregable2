

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
 path('Pedidos/', include('Pedidos.urls')),
 path('admin/', admin.site.urls),
]