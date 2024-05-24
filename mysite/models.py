from django.db import models


# Create your models here.
class indexmodel(models.Model):
    img = models.ImageField(upload_to='pics', null=True, blank=True)


class usermsg(models.Model):
    name = models.EmailField(max_length=50, null=False)
    email = models.EmailField(max_length=50, null=False)
    phone = models.IntegerField()
    subject = models.CharField(max_length=50, null=False)
    msg = models.CharField(max_length=200, null=False)

    def __str__(self):
        return self.name


class booking(models.Model):
    Patientname = models.CharField(max_length=50, null=False)
    Phonenumber = models.IntegerField()
    EmailId = models.EmailField(max_length=50, null=False)
    Doctorname = models.EmailField(max_length=50, null=False)
    Bookingdate = models.DateField()

    def __str__(self):
        return self.Patientname


class doctordata(models.Model):
    img = models.ImageField(upload_to='pics', null=True, blank=True)
    name = models.CharField(max_length=80, null=False)
    department = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class department(models.Model):
    departmentname = models.CharField(max_length=80, null=False)
    about = models.TextField(null=False)


    def __str__(self):
        return self.departmentname


class About(models.Model):
    img = models.ImageField(upload_to='pics', null=True, blank=True)




