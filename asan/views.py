from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
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


def process(request):
  if request.method == 'POST':
    # Get the selected product IDs
    selected_items = request.POST.getlist('selected_items[]')

    # Validate and convert IDs to integers
    try:
        selected_ids = [int(product_id) for product_id in selected_items]
    except ValueError:
        return JsonResponse({"error": "Invalid product ID"}, status=400)

    # Get the list of counts
    counts = request.POST.getlist('counts[]')

    # Convert counts to integers
    try:
        counts = [int(count) for count in counts]
    except ValueError:
        return JsonResponse({"error": "Invalid count value"}, status=400)

    # Pair product IDs with counts
    data = zip(selected_ids, counts)

    # Calculate the total price
    total_price = 0
    detailed_items = []
    from .models import Mehsullar

    for product_id, count in data:
        try:
            product = Mehsullar.objects.get(id=product_id)
            item_total = product.standart_satis * count
            total_price += item_total
            detailed_items.append({
                "mehsul_adi": product.mehsul_adi,
                "sayi": count,
                "mehsul_qiymeti": item_total
            })
        except Mehsullar.DoesNotExist:
            pass  # Handle missing product

    context = {
        "umumi_qiymet": total_price,
        "secilmis_mehsullar": detailed_items
    }
    return render(request, 'asan/process.html', context=context)