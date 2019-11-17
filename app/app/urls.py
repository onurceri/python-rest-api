from django.contrib import admin
from django.urls import path, re_path, include
from core.views.login_view import login
from core.views.register_view import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', login, name="user-login-api"),
    path('api/register', register, name="user-register-api"),
    re_path('api/(?P<version>(v1|v2))/', include('customer.urls')),
    re_path(r'^', include('customer.urls')),
]
