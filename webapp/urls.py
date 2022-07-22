from . import views
from .views import index, uploadedvideos
from django.urls import path
urlpatterns = [
    
    path('',index, name= 'home'),
    path('uploadedvideos',views.uploadedvideos, name= 'uploadedvideos'),
    path('charges',views.charges, name= 'charges'),
    path('price',views.price, name= 'price'),
]
