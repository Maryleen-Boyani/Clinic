from django.shortcuts import render
from rest_framework import generics
from django.http import HttpResponse

from .serializers import (
    DoctorSerializer,
    PatientSerializer,
    AppointmentsSerializer,
    DepartmentsSerializer,
    VisitsSerializer,
    LoginSerializer
)
from .models import Doctor, Patient, Appointments, Departments, Visits, Login


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the Appointment index.")

class DoctorDetailsView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()  # selects all from the model Doctor
    serializer_class = DoctorSerializer


class PatientListView(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class AppointmentsDetailsView(generics.ListCreateAPIView):
    queryset = Appointments.objects.all()
    serializer_class = AppointmentsSerializer


class DepartmentsDetailsView(generics.ListCreateAPIView):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer


class VisitsListView(generics.ListCreateAPIView):
    queryset = Visits.objects.all()
    serializer_class = VisitsSerializer

class LoginListView(generics.ListCreateAPIView):
    queryset = Login.objects.all()
    serializer_class = LoginSerializer