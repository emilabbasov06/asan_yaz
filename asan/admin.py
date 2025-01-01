from django.contrib import admin
from . import models

# Register your models here.
class FirmalarAdmin(admin.ModelAdmin):
  list_display = ('firma_adi', 'magaza')

class MehsullarAdmin(admin.ModelAdmin):
  list_display = ('mehsul_adi', 'firma', 'magaza', 'standart_satis', 'top_alis', 'satis')
  list_filter = ('kategoriya', 'magaza')

class MagazalarAdmin(admin.ModelAdmin):
  list_display = ('magaza_adi', 'unvan', 'elaqe', 'email', 'instagram')

admin.site.register(models.Firmalar, FirmalarAdmin)
admin.site.register(models.Mehsullar, MehsullarAdmin)
admin.site.register(models.Magazalar, MagazalarAdmin)
admin.site.register(models.Kategoriya)