from django.urls import path
from .import views as v

urlpatterns = [
    path('' , v.home , name="home"),
    path('about/' , v.about , name="about"),
    path('blog/' , v.blog , name="blog"),
    path('login/' , v.log , name="log"),
    path('contact/' , v.contact , name="contact"),
    path('regn/' , v.usregn , name="usregn"),
    path('uslgin/' , v.uslgin , name="uslgin"),
    path('vdlgin/' , v.vdlgin , name="vdlgin"),
    path('addpackage/' , v.packagedetails , name="addpackage"),
    path('item/<int:pk>/edit/' , v.vendoredit , name="edit"),
    path('item/<int:pk>/delete/' , v.deletepackage , name="del"),
    path('vendor/' , v.vendor , name="vendor"),
    path('userpage/' , v.userpage , name="user"),
    path('vdlogout/' , v.vendorlogout , name="vdlogout"),
    path('uslogout/' , v.userlogout , name="uslogout"),
    path('approved/' , v.approved , name="approved"),
    path('pending/' , v.pending , name="pending"),
    path('back/' , v.back , name="back"),
    path('backk/' , v.backk , name="backk"),
    path('booknow/<int:pk>/package/' , v.booknow , name="booknow"),
    path('payment/' , v.payment , name="payment"),
    path('bookingdetails/' , v.userbookingdetails , name="bookingdetails"),
    path('userbookingpackages/<int:pk>/packagess/' , v.userbookingpackages , name="bookedpackage"),
]


