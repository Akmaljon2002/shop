from django.contrib.auth.models import User
from django.db import models

class Foydalanuvchi(models.Model):
    ism = models.CharField(max_length=20)
    fam = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tel = models.CharField(max_length=15, blank=True, null=True)
    rasm = models.ImageField(blank=True, null=True)
    def __str__(self):
        return self.ism

class Filial(models.Model):
    nom = models.CharField(max_length=50)
    manzil = models.CharField(max_length=60, blank=True, null=True)
    def __str__(self):
        return self.nom

class Taminotchi(models.Model):
    fish = models.CharField(max_length=60, blank=True, null=True)
    nom = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=15, blank=True, null=True)
    manzil = models.CharField(max_length=50, blank=True, null=True)
    active = models.BooleanField(default=True)
    qarz = models.IntegerField(default=0)
    def __str__(self):
        return self.fish


class Sotuvchi(models.Model):
    fish = models.CharField(max_length=60, blank=True, null=True)
    tel = models.CharField(max_length=15, blank=True, null=True)
    manzil = models.CharField(max_length=100, blank=True, null=True)
    rasm = models.ImageField(blank=True, null=True)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    qr_code = models.PositiveIntegerField(blank=True, null=True, unique=True)
    def __str__(self):
        return self.fish


class Mijoz(models.Model):
    fish = models.CharField(max_length=60, blank=True, null=True)
    manzil = models.CharField(max_length=50, blank=True, null=True)
    tel = models.CharField(max_length=15, blank=True, null=True)
    qarz = models.IntegerField(default=0)
    def __str__(self):
        return self.fish


class Mahsulot(models.Model):
    nom = models.CharField(max_length=50, blank=True, null=True)
    brand = models.CharField(max_length=50, blank=True, null=True)
    sana = models.DateField(auto_now_add=True)
    bar_code = models.PositiveIntegerField(blank=True, null=True)
    tan_narx = models.PositiveIntegerField(blank=True, null=True)
    narx = models.PositiveIntegerField(blank=True, null=True)
    foiz = models.SmallIntegerField(blank=True, null=True)
    mijoz = models.ForeignKey(Taminotchi, on_delete=models.CASCADE)
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE)
    rasm = models.ImageField(blank=True, null=True)
    miqdor = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.nom


class Sotuv(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    sotuvchi = models.ForeignKey(Sotuvchi, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField(default=1)
    narx = models.PositiveIntegerField(blank=True, null=True)
    tolandi = models.PositiveIntegerField(blank=True, null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE, blank=True, null=True)
    qoldi = models.IntegerField(default=0)
    sana = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.mahsulot