from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DepartmentViewSet,
    EmployeeViewSet,
    AchievementViewSet,
    UpdateEmployee,
    DeleteEmployee
)

# DRF Router for API endpoints
router = DefaultRouter()
router.register("departments", DepartmentViewSet, basename="departments")
router.register("employees", EmployeeViewSet, basename="employees")
router.register("achievements", AchievementViewSet, basename="achievements")

# URL patterns for CRUD actions
urlpatterns = [
    path("employee/<int:emp_id>/update/", UpdateEmployee.as_view(), name="update_employee"),
    path("employee/<int:emp_id>/delete/", DeleteEmployee.as_view(), name="delete_employee"),

    # Include API routes from router
    path("", include(router.urls)),
]
