from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    package = Package.objects.all()
    return render(request , 'home.html' , {'package':package})

def about(request):
    return render(request , 'about.html')

def blog(request):
    return render(request , 'blog.html')

def contact(request):
    return render(request , 'contact.html')

def log(request):
    return render(request , 'login.html')

def vendor(request):
    vendor_id = request.session.get('vendor.id')
    vendor = Vendorregistration.objects.get(id=vendor_id)
    package = Package.objects.filter(vendor=vendor_id)
    return render(request , 'vendor.html', {'vendor':vendor ,'package':package})

def userpage(request):
    userr_id = request.session.get('user.id')
    user = Userregistration.objects.get(id=userr_id)
    package = Package.objects.all()
    return render(request,'user.html',{'user':user , 'package':package})

def vendorlogout(request):
    logout(request)
    return redirect("home")
    
def userlogout(request):
    logout(request)
    return redirect("home")

def usregn(request):
    if request.method =='POST':
        form1 = Userregisterform(request.POST)
        form2 = Vendorregisterform(request.POST)
        if form1.is_valid() :
            user = form1.save(commit=False)
            user.Password = make_password(user.Password)
            user.save()
            return redirect('home')
        elif form2.is_valid():
            vendor = form2.save(commit=False)
            vendor.Password = make_password(vendor.Password)
            vendor.save()
            return redirect('home')
    else:
        form1 = Userregisterform()
        form2 = Vendorregisterform()
    return render (request , 'usregn.html' , {'form1':form1 , 'form2':form2})

def uslgin(request):
    if request.method == 'POST':
        form = Usloginform(data = request.POST)
        if form.is_valid():
            Username = form.cleaned_data.get('Username')
            Password = form.cleaned_data.get('Password')
            try:
                user = Userregistration.objects.get(Username=Username)
                if check_password(Password , user.Password):
                    request.session['user.id'] = user.id
                    return redirect('userpage')
                else:
                    return render(request , 'uslgin.html' , {'form':form , 'error':'Invalid Password'})
            except Userregistration.DoesNotExist:
                return render(request , 'uslgin.html' , {'form':form , 'error':'User Does not exist'})
    else:
        form = Usloginform()
    return render(request , 'uslgin.html' , {'form':form})

def vdlgin(request):
    if request.method == 'POST':
        form = Vdloginform(data = request.POST)
        if form.is_valid():
            Username = form.cleaned_data.get('Username')
            Password = form.cleaned_data.get('Password')
            try:
                vendor = Vendorregistration.objects.get(Username=Username)
                if check_password(Password , vendor.Password):
                    request.session['vendor.id'] = vendor.id
                    return redirect('vendor')
                else:
                    return render(request , 'vdlgin.html' , {'form':form , 'error':'Invalid Password'})
            except Vendorregistration.DoesNotExist:
                return render(request , 'vdlgin.html' , {'form':form , 'error':'User Does not exist'})
    else:
        form = Vdloginform()
    return render(request , 'vdlgin.html' , {'form':form})

def packagedetails(request):
    if request.method == 'POST':
        form = Packagedetailsform(request.POST , request.FILES)
        if form.is_valid():
            vendor_id = request.session.get('vendor.id')
            vendorr = Vendorregistration.objects.get(id=vendor_id)
            vendor = vendorr.id
            packagee = form.save(commit=False)
            packagee.vendor = vendor
            packagee.save()
            return redirect('vendor')
    else :
        form = Packagedetailsform()
        vendor_id = request.session.get('vendor.id')
        vendor = Vendorregistration.objects.get(id=vendor_id)
    return render (request , 'packagedetails.html' , {'vendor':vendor ,'form':form})

def vendoredit(request, pk):
    item = get_object_or_404(Package, pk=pk)
    if request.method == 'POST':
        form = Packagedetailsform(request.POST , instance=item)
        if form.is_valid():
            form.save()
            return redirect("vendor")
    else:
        form = Packagedetailsform(instance=item)
    return render(request, 'editdisplay.html', {'form':form})

def deletepackage(request , pk):
    item = get_object_or_404(Package , pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('vendor')
    else:
        return render(request , 'vendor.html')
    
def booknow(request,pk):
    item = get_object_or_404(Package , pk=pk)
    if request.method == 'POST':
        form = Booknowform(request.POST)
        if form.is_valid():
            user_id = request.session.get('user.id')
            userr = get_object_or_404(Userregistration , id = user_id)
            formm = form.save(commit=False)
            formm.user = userr
            formm.package = item
            request.session[pk] = item.pk
            formm.save()
            return redirect('payment')
    else :
        form = Booknowform()
        userr_id = request.session.get('user.id')
        user = Userregistration.objects.get(id=userr_id)
    return render(request , 'booknow.html' , {'user':user , 'form':form})

def approved(request):
    vendor_id = request.session.get('vendor.id')
    vendor = Vendorregistration.objects.get(id=vendor_id)
    package = Package.objects.filter(vendor=vendor_id)
    return render(request , 'homeapproved.html' , {'vendor':vendor , 'package':package})

def pending(request):
    vendor_id = request.session.get('vendor.id')
    vendor = Vendorregistration.objects.get(id=vendor_id)
    package = Package.objects.filter(vendor=vendor_id)
    return render(request , 'homepending.html' , {'vendor':vendor ,'package':package})

def back(request):
    return redirect('vendor')

def backk(request):
    return redirect('userbookingdetails')

def payment(request):
    userr_id = request.session.get('user.id')
    user = Userregistration.objects.get(id=userr_id)
    return render (request , 'payment.html' ,{'user':user})

def userbookingdetails(request):
    vendor_id = request.session.get('vendor.id')
    vendor = Vendorregistration.objects.get(id=vendor_id)
    packages = Package.objects.filter(vendor=vendor_id)
    booking = Booknow.objects.filter(package__in=packages).select_related('package','user')
    return render(request , 'bookingdetails.html', {'vendor':vendor ,'booking':booking})

def userbookingpackages(request , package_id):
    vendor_id = request.session.get('vendor.id')
    vendor = Vendorregistration.objects.get(id=vendor_id)
    vendorr = get_object_or_404(Vendorregistration ,id=vendor_id )
    packages = get_object_or_404(Package , id=package_id ,vendor=vendorr.id)
    booking =  Booknow.objects.filter(package=packages).select_related('user')
    return render(request , 'bookingpackage.html', {'vendor':vendor ,'package':packages , 'booking':booking})

def userpackages(request):
    user_id = request.session.get('user.id')
    user = Userregistration.objects.get(id=user_id)
    booking = Booknow.objects.filter(user_id=user_id)
    return render(request , 'userpackages.html',{'user':user , 'booking':booking})
    