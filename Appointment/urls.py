from django.urls import path
from .views import DoctorDetailsView, PatientListView

urlpatterns =[
    path("Doctor/", DoctorDetailsView.as_view()),
    path("Patient/", PatientListView.as_view()),
]