from django.db import models


# Create your models here.
# Doctors model
class Doctor(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phonenumber = models.IntegerField()
    staffid = models.IntegerField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return str(self.staffid)


class Patient(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phonenumber = models.IntegerField()
    idnumber = models.IntegerField()

    def __str__(self):
        return str(self.idnumber)


class Appointments(models.Model):
    Patient_IDnumber = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor_Staffid = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.department


class Departments(models.Model):
    name = models.CharField(max_length=50)
    dep_id = models.IntegerField()

    def __str__(self):
        return self.name


class Visits(models.Model):
    Doctor_staffid = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    Patient_idnumber = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    doctors_notes = models.TextField()
    triage_notes = models.TextField()

    def __str__(self):
        return self.Doctor_staffid  # returns the doctor's staff id


class Login(models.Model):

    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email
