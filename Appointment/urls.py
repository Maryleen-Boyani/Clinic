from django.urls import path

from .views import (
    index,
    DoctorDetailsView,
    PatientListView,
    AppointmentsDetailsView,
    DepartmentsDetailsView,
    VisitsListView,
    LoginListView
)

urlpatterns = [
    path("", index, name="index"),
    path("Doctor/", DoctorDetailsView.as_view()),
    path("Patient/", PatientListView.as_view()),
    path("Appointments/", AppointmentsDetailsView.as_view()),
    path("Departments/", DepartmentsDetailsView.as_view()),
    path("Visits/", VisitsListView.as_view()),
    path("Login/", LoginListView.as_view())
]
