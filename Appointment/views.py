from django.shortcuts import render
from rest_framework import generics

from .serializers import DoctorSerializer, PatientSerializer
from .models import Doctor, Patient


# Create your views here.
class DoctorDetailsView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()# selects all from the model Doctor
    serializer_class = DoctorSerializer

class PatientListView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class =  PatientSerializer
