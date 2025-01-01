from django.shortcuts import render
from django.http import HttpResponse
from .models import Firmalar, Magazalar, Mehsullar, Kategoriya

# Create your views here.
def index(request):
  mehsullar = Mehsullar.objects.all()
  kategoriyalar = Kategoriya.objects.all()
  context = {
    'mehsullar': mehsullar,
    'kategoriyalar': kategoriyalar
  }
  return render(request, 'asan/index.html', context=context)


def firmalar(request):
  all_firmalar = Firmalar.objects.all()
  magazalar = Magazalar.objects.all()

  context = {
    'firmalar': all_firmalar,
    'magazalar': magazalar
  }

  return render(request, 'asan/firmalar.html', context=context)


def firma(request, firma_adi):
  firma_object = Firmalar.objects.get(firma_adi=firma_adi)
  
  context = {
    'firma': firma_object
  }
  
  return render(request, 'asan/firma.html', context=context)