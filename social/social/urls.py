
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Basic Admin page included with Django
    path('admin/', admin.site.urls),
    # Account URLS
    path('account/', include('account.urls')),
]
