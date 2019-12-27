from django.conf import settings
from django.urls import include, path
from . import views
from django.conf.urls.static import static
from .views import GeneratePDF
from .views import Patient
from django.views.generic import TemplateView
urlpatterns = [
        path('', views.index, name='index'),
       # path('admin', views.admin, name='admin'),
        path('product/', views.product, name='product'),
        path('book/', views.book, name='book'),
        path('appoint/', views.appoint, name='appoint'),
        path('contact/', views.contact, name='contact'),
        path('login/', views.login, name='login'),
        path('loginForm/', views.loginForm, name='loginForm'),
        path('alogin/', views.alogin, name='alogin'),
        path('aloginForm/', views.aloginForm, name='aloginForm'),
        path('register/', views.register, name='register'),
        path('registerForm/', views.registerForm, name='registerForm'),
        path('cart/', views.cart, name='cart'),
        path('YourCart/', views.YourCart, name='YourCart'),
        path('addToCart/', views.addToCart, name='addToCart'),
        path('category/', views.category, name='category'),
        path('aboutproduct/', views.aboutproduct, name='aboutproduct'),
        path('admin/', views.admin, name='admin'),
        path('logout/', views.logout, name='logout'),
        path('alogout/', views.alogout, name='alogout'),
        path('addItem/', views.addItem, name='addItem'),
        path('caddItem/', views.caddItem, name='caddItem'),
        path('removeItem/', views.removeItem, name='removeItem'),
        path('removeFromCart/', views.removeFromCart, name='removeFromCart'),
        path('clearcart/', views.clearcart, name='clearcart'),
        path('aregister/', views.aregister, name='aregister'),
        path('aregisterForm/', views.aregisterForm, name='aregisterForm'),
        path('update/<productId>', views.update, name='update'),
        path('DoctorRegister/', views.DoctorRegister, name='DoctorRegister'),
        path('DoctorLogin/', views.DoctorLogin, name='DoctorLogin'),
        path('DoctorLoginForm/', views.DoctorLoginForm, name='DoctorLoginForm'),
        path('DoctorPage/', views.DoctorPage, name='DoctorPage'),
        path('DoctorLogout/', views.DoctorLogout, name='DoctorLogout'),
        path('DoctorDetail/', views.DoctorDetail, name='DoctorDetail'),
        path('CancelAppointment/', views.CancelAppointment, name='CancelAppointment'),
        path('file/', views.file , name='file '),
        path('about/', views.about , name='about'),
        #path('pdf/', views.getpdf , name='pdf'),
        path('pdf/', GeneratePDF.as_view() ),
        path('ppdf/', Patient.as_view() ),
        path('report/', views.report , name='report'),
        path('patient/', views.patient , name='patient'),

        path('ConfirmAppointment/', views.ConfirmAppointment, name='ConfirmAppointment'),
        #path('bKash_payment/', views.bkash, name='bkash'),
]   +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)