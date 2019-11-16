from django.contrib import admin
from django.urls import path, re_path, include
from core import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', login_view.login),
    re_path('api/(?P<version>(v1|v2))/', include('customer.urls'))
]
