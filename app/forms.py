from django import forms
from .models import *


class Userregisterform(forms.ModelForm):
    class Meta:
        model = Userregistration
        fields = ['First_Name','Last_Name','Email','Phone_Number','Place','Username','Password']


class Vendorregisterform(forms.ModelForm):
    class Meta:
        model = Vendorregistration
        fields = ['Full_Name','Company_name', 'Phone_Number','Year_established', 'Username','Password','Address']
        

class Usloginform(forms.Form):
    Username = forms.CharField(max_length=100 )
    Password = forms.CharField(widget=forms.PasswordInput)

class Vdloginform(forms.Form):
    Username = forms.CharField(max_length=100 )
    Password = forms.CharField(widget=forms.PasswordInput)

class Packagedetailsform(forms.ModelForm):
    class Meta :
        model = Package
        fields = ['Package_place' , 'days_stay' , 'price_per_person' , 'Image_related_to_package', 'Description']
        

class Booknowform(forms.ModelForm):
    class Meta:
        model = Booknow
        fields = ['Full_Name' , 'Contact_Number' , 'Email' , 'No_of_persons' , 'No_of_Childrens' , 'Booking_reservation_date']
        


