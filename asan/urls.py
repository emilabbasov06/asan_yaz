from django.urls import path
from . import views

urlpatterns = [
    # /
    # /firmalar
    # /firmalar/<str:firma_adi>
    path('', views.index, name='home'),
    path('firmalar/', views.firmalar, name='firmalar'),
    path('firma/<str:firma_adi>', views.firma, name='firma')
]
