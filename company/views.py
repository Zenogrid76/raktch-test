from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee, Department
from achievements.models import Achievement
from rest_framework import viewsets, permissions
from .serializers import EmployeeSerializer, DepartmentSerializer
from achievements.serializers import AchievementSerializer
from django.db import IntegrityError


##### ----- TEMPLATE VIEWS ----- #####

class DashboardPage(View):
    def get(self, request):
        if not request.session.get("access"):
            return redirect("login_page")
        
        user_email = request.session.get("user_email", "User")
        
        employees = Employee.objects.select_related("department").prefetch_related("achievements")
        departments = Department.objects.all()
        achievements = Achievement.objects.all()

        return render(request, "dashboard.html", {
            "user_email": user_email,
            "employees": employees,
            "departments": departments,
            "achievements": achievements,
        })

    def post(self, request):
        try:
            
            if "department_name" in request.POST:
                Department.objects.create(name=request.POST["department_name"])

            
            elif "achievement_name" in request.POST:
                Achievement.objects.create(name=request.POST["achievement_name"])

            
            elif "employee_name" in request.POST:
                email = request.POST["employee_email"].strip()

            #check if email already exists  
                if Employee.objects.filter(email=email).exists():
                    return render(request, "dashboard.html", {
                        "error": f"Employee with email {email} already exists.",
                        "user_email": request.session.get("user_email", "User"),
                        "employees": Employee.objects.all(),
                        "departments": Department.objects.all(),
                        "achievements": Achievement.objects.all(),
                    })

                dept = Department.objects.get(id=request.POST["department"])
                employee = Employee.objects.create(
                    name=request.POST["employee_name"],
                    email=email,
                    phone=request.POST.get("employee_phone", ""),
                    address=request.POST.get("employee_address", ""),
                    department=dept,
                )
                ach_ids = request.POST.getlist("employee_achievements")
                if ach_ids:
                    employee.achievements.add(*ach_ids)
        #Except block for IntegrityError
        except IntegrityError:
            return render(request, "dashboard.html", {
                "error": "Database integrity error. Please check your input.",
                "user_email": request.session.get("user_email", "User"),
                "employees": Employee.objects.all(),
                "departments": Department.objects.all(),
                "achievements": Achievement.objects.all(),
            })

        return redirect("dashboard_page")


##### ----- API VIEWS  ----- #####
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
    permission_classes = [permissions.IsAuthenticated]


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().select_related("department").prefetch_related("achievements")
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]


# Update Employee
class UpdateEmployee(View):
    def get(self, request, emp_id):
        employee = get_object_or_404(Employee, id=emp_id)
        departments = Department.objects.all()
        achievements = Achievement.objects.all()
        return render(request, "update_employee.html", {
            "employee": employee,
            "departments": departments,
            "achievements": achievements,
        })

    def post(self, request, emp_id):
        employee = get_object_or_404(Employee, id=emp_id)
        employee.name = request.POST["employee_name"]
        employee.email = request.POST["employee_email"]
        employee.phone = request.POST.get("employee_phone", "")
        employee.address = request.POST.get("employee_address", "")
        employee.department = Department.objects.get(id=request.POST["department"])
        employee.save()

        ach_ids = request.POST.getlist("employee_achievements")
        if ach_ids:
            employee.achievements.set(ach_ids)
        else:
            employee.achievements.clear()

        return redirect("dashboard_page")


# Delete Employee
class DeleteEmployee(View):
    def post(self, request, emp_id):
        employee = get_object_or_404(Employee, id=emp_id)
        employee.delete()
        return redirect("dashboard_page")