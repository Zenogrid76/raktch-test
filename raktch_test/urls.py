from django.urls import path, include
from django.contrib import admin
from django.views.generic import RedirectView
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    RegisterView,
    CustomTokenObtainPairView,
    LogoutView,
    SignupPage,
    LoginPage,
    LogoutRedirect
)
from company.views import DashboardPage

urlpatterns = [
    # Root redirects to login page
    path("", RedirectView.as_view(url="/login/")),

    # Admin
    path("admin/", admin.site.urls),

    # Authentication APIs
    path("api/auth/signup/", RegisterView.as_view(), name="signup_api"),
    path("api/auth/login/", CustomTokenObtainPairView.as_view(), name="login_api"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh_api"),
    path("api/auth/logout/", LogoutView.as_view(), name="logout_api"),

    # UI pages
    path("signup/", SignupPage.as_view(), name="signup_page"),
    path("login/", LoginPage.as_view(), name="login_page"),
    path("dashboard/", DashboardPage.as_view(), name="dashboard_page"),
    path("logout/", LogoutRedirect.as_view(), name="logout_page"),

    # Include company app URLs (API + CRUD)
    path("api/", include("company.urls")),
]
