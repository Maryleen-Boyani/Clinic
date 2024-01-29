from django.db import models


# Create your models here.
# Doctors model
class Doctor(models.Model):
    firstname = models.charField(max_length=50)
    lastname = models.charField(max_length=50)
    email = models.emaiField(max_length=50)
    phone = models.IntegerField
    staffid = models.IntegerField
    department = models.charField(max_length=50)

    def __str__(self):
        return self.firstname


class Patient(models.Model):
    firstname = models.charField(max_length=50)
    lastname = models.charField(max_length=50)
    email = models.emaiField(max_length=50)
    phone = models.IntegerField
    idnumber = models.IntegerField


def __str__(self):
    return self.firstname


class Appointments(models.Model):
    fk_idnumber = models.ForeignKey(Patient, on_delete=models.CASCADE)
    fk_staffid = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.date


class Departments(models.Model):
    name = models.CharField(max_length=50)
    dep_id = models.IntegerField

    def __str__(self):
        return self.name


class Visits(models.Model):
    fk_staffid = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fk_idnumber = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField
    doctors_notes = models.TextField
    triage_notes = models.TextField

    def __str__(self):
        return self.date


class Login(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.email
