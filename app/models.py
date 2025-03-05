from django.db import models

# Create your models here.

class Userregistration(models.Model):
    First_Name = models.CharField(max_length=50)
    Last_Name = models.CharField(max_length=50)
    Email = models.EmailField()
    Phone_Number = models.CharField(max_length=15 , default=0)
    Place = models.CharField(max_length=100 , default=0)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

class Vendorregistration(models.Model):
    Full_Name = models.CharField(max_length=100)
    Company_name = models.CharField(max_length=150 , default=0)
    Address = models.TextField(default=0)
    Phone_Number = models.CharField(max_length=15 , default=0)
    Year_established = models.PositiveBigIntegerField(default=0)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

class Package(models.Model):
    vendor = models.IntegerField(default=0)
    Package_place = models.CharField(max_length=100)
    days_stay = models.CharField(max_length=200)
    price_per_person = models.CharField(max_length=100 , default=0)
    Description = models.TextField(max_length=500 , default=0)
    Image_related_to_package = models.ImageField(upload_to='gallery/')
    is_approved = models.BooleanField(default=False)

class Booknow(models.Model):
    package = models.ForeignKey(Package ,on_delete=models.CASCADE)
    user = models.ForeignKey(Userregistration,on_delete=models.CASCADE)
    Full_Name = models.CharField(max_length=100)
    Contact_Number = models.CharField(max_length=15)
    Email = models.EmailField(default=0)
    No_of_persons = models.IntegerField()
    No_of_Childrens = models.CharField(max_length=50 , default=0)
    Booking_reservation_date = models.DateField()