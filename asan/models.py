from django.db import models

# Create your models here.
class Magazalar(models.Model):
  magaza_adi = models.CharField(max_length=100)
  unvan = models.CharField(max_length=200)
  elaqe = models.CharField(max_length=20)
  email = models.EmailField(max_length=254)
  instagram = models.CharField(max_length=100)
  
  def __str__(self):
    return f'{self.magaza_adi}'
  
  class Meta:
    verbose_name_plural = 'Magazalar'


class Firmalar(models.Model):
  firma_adi = models.CharField(max_length=100)
  haqqinda = models.TextField(blank=True)
  magaza = models.ForeignKey(Magazalar, on_delete=models.SET_NULL, null=True)
  
  def __str__(self):
    return f'{self.firma_adi}'
  
  class Meta:
    verbose_name_plural = 'Firmalar'


class Mehsullar(models.Model):
  mehsul_adi = models.CharField(max_length=200)
  firma = models.ForeignKey(Firmalar, on_delete=models.CASCADE)
  magaza = models.CharField(max_length=100)
  standart_satis = models.FloatField()
  top_alis = models.FloatField()
  satis = models.FloatField()
  
  def __str__(self):
    return f'{self.mehsul_adi}'
  
  class Meta:
    verbose_name_plural = 'Mehsullar'
