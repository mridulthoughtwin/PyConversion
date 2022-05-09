from django.contrib import admin
from django.urls import path , include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('currency/',include('currency.urls')),
    path('documents/',include('docum.urls')),
]
