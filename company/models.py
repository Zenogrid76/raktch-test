from django.db import models
from achievements.models import Achievement

#Department Model
class Department(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'Department'

    def __str__(self):
        return self.name

#Employee Model with name, email, phone, address, department (ForeignKey to Department), achievements (ManyToManyField to Achievement through Pivot)
class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    address = models.TextField(blank=True)
    department = models.ForeignKey(
        Department, 
        on_delete=models.CASCADE, 
        related_name='employees'
    )
    achievements = models.ManyToManyField(
        Achievement,
        through='Pivot',
        related_name='employees',
        blank=True
    )

    class Meta:
        db_table = 'Employee'

    def __str__(self):
        return self.name

# Pivot Model to link Employee and Achievement with achievement_date
class Pivot(models.Model):
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    achievement_date = models.DateField()

    class Meta:
        db_table = 'Pivot'
        constraints = [
            models.UniqueConstraint(
                fields=['achievement', 'employee', 'achievement_date'], 
                name='unique_achievement_employee_date'
            )
        ]

    def __str__(self):
        return f"{self.employee.name} - {self.achievement.name} on {self.achievement_date}"
