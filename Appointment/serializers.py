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

class AppointmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = ("Patient_IDnumber", "date", "Doctor_Staffid")

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ("name", "dep_id")

class VisitsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Visits
        fields= ("Doctor_staffid", "Patient_idnumber", "doctors_notes", "date")

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields =("email", "password")