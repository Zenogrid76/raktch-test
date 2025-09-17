from django.urls import path
from django.contrib import admin
from .views import DashboardPage, RegisterView, LogoutView, SignupPage, LoginPage,LogoutRedirect, CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/login/")),
    path("admin/", admin.site.urls),

    # API endpoints
    path("api/auth/signup/", RegisterView.as_view(), name="signup_api"),
    path("api/auth/login/", CustomTokenObtainPairView.as_view(), name="login_api"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh_api"),
    path("api/auth/logout/", LogoutView.as_view(), name="logout_api"),

    # UI pages
    path("signup/", SignupPage.as_view(), name="signup_page"),
    path("login/", LoginPage.as_view(), name="login_page"),
    path("dashboard/", DashboardPage.as_view(), name="dashboard_page"),
    path("logout/", LogoutRedirect.as_view(), name="logout_page"),

]
