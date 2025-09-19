from rest_framework import serializers
from .models import Employee, Department, Pivot
from achievements.models import Achievement

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = "__all__"


class PivotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pivot
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source="department", write_only=True
    )
    achievements = AchievementSerializer(many=True, read_only=True)
    achievement_ids = serializers.PrimaryKeyRelatedField(
        queryset=Achievement.objects.all(),
        many=True,
        write_only=True,
        required=False
    )

    class Meta:
        model = Employee
        fields = [
            "id", "name", "email", "phone", "address",
            "department", "department_id",
            "achievements", "achievement_ids"
        ]

    def create(self, validated_data):
        achievements = validated_data.pop("achievement_ids", [])
        employee = Employee.objects.create(**validated_data)
        for achievement in achievements:
            Pivot.objects.create(employee=employee, achievement=achievement, achievement_date="2025-01-01")
        return employee

    def update(self, instance, validated_data):
        achievements = validated_data.pop("achievement_ids", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        if achievements is not None:
            instance.achievements.clear()
            for achievement in achievements:
                Pivot.objects.create(employee=instance, achievement=achievement, achievement_date="2025-01-01")
        return instance
