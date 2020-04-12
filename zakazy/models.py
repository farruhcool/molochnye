from django.db import models
from produkty.models import Produkt
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Status(models.Model):
    name=models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated= models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Статус %s" % self.name

    class Meta:
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Статусы заказа'



class Zakaz(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None,on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)  #total price for all products in zakaz
    customer_name=models.CharField(max_length=66, blank=True, null=True, default=None)
    customer_email=models.EmailField(blank=True, null=True, default=None)
    customer_phone=models.CharField(max_length=50, blank=True, null=True, default=None)
    customer_address=models.CharField(max_length=128, blank=True, null=True, default=None)
    comments = models.TextField(blank=True, null=True, default=None)
    status = models.ForeignKey(Status,on_delete=models.CASCADE)
    created= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated= models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Заказ %s" % (self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):

        super(Zakaz, self).save(*args, **kwargs)

class ProductInOrder(models.Model):
    zakaz = models.ForeignKey(Zakaz, blank=True, null=True, default=None,on_delete=models.CASCADE)
    produkt = models.ForeignKey(Produkt, blank=True, null=True, default=None,on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)#price*nmb
    is_active = models.BooleanField(default=True)
    created= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated= models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.produkt.name

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
         price_per_item=self.produkt.price
         self.price_per_item = price_per_item
         print(self.nmb)
         self.total_price=int(self.nmb)*price_per_item


         super(ProductInOrder, self).save(*args, **kwargs)


def product_in_zakaz_post_save(sender, instance, created, **kwargs):
    zakaz = instance.zakaz
    all_products_in_zakaz = ProductInOrder.objects.filter(zakaz=zakaz, is_active=True)

    zakaz_total_price = 0
    for item in all_products_in_zakaz:
        zakaz_total_price += item.total_price

    instance.zakaz.total_price = zakaz_total_price
    instance.zakaz.save(force_update=True)


post_save.connect(product_in_zakaz_post_save, sender=ProductInOrder)



class ProductInBasket(models.Model):
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    zakaz = models.ForeignKey(Zakaz, blank=True, null=True, default=None,on_delete=models.CASCADE)
    produkt = models.ForeignKey(Produkt, blank=True, null=True, default=None,on_delete=models.CASCADE)
    nmb = models.IntegerField(default=1)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)#price*nmb
    is_active = models.BooleanField(default=True)
    created= models.DateTimeField(auto_now_add=True, auto_now=False)
    updated= models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.produkt.name

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'


    def save(self, *args, **kwargs):
        # if hasattr(ProductInOrder, 'price'):
            price_per_item = self.produkt.price
            self.price_per_item = price_per_item
            self.total_price = int(self.nmb) * price_per_item

            super(ProductInBasket, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #       price_per_item=self.produkt.price
    #       self.price_per_item = price_per_item
    #
    #       self.total_price=self.nmb*price_per_item
    #
    #
    #      super(ProductInBasket, self).save(*args, **kwargs)
