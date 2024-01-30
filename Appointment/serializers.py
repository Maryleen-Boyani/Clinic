from .models import Doctor, Patient, Appointments, Departments, Visits, Login
from rest_framework import serializers

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Doctor
        fields = ("firstname", "lastname")

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("firstname", "email", "phonenumber")

