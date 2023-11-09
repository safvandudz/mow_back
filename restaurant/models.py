from django.db import models
from user.models import User

class StoreOwner(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)



    class Meta:
        db_table = 'restuarant_store_owner' 
        verbose_name = 'store owner'
        verbose_name_plural = 'store owners'
        ordering = ["-id"]

    def __str__(self):
        return self.user.phone_number
    
class StoreCategory(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')


    class Meta:
        db_table = 'restuarant_store_category' 
        verbose_name = 'store_category'
        verbose_name_plural = 'store_categorys'
        ordering = ["-id"]

    def __str__(self):
        return self.name



class Restaurant(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    category=models.ManyToManyField(StoreCategory)
    tagline=models.CharField(max_length=50)
    rate=models.IntegerField(blank=True,null=True)
    owner=models.ForeignKey(StoreOwner,on_delete=models.CASCADE)

    class Meta:
        db_table = 'restuarant_restaurant' 
        verbose_name = 'restaurant'
        verbose_name_plural = 'restaurants'
        ordering = ["-id"]

    def __str__(self):
        return self.name





class FoodCategory(models.Model):
    name=models.CharField(max_length=100)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    
    class Meta:
        db_table = 'restuarant_food_category' 
        verbose_name = 'food_category'
        verbose_name_plural = 'food_categorys'
        ordering = ["-id"]

    def __str__(self):
        return self.name


class Food(models.Model):
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images/')
    category=models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    price=models.IntegerField(blank=True,null=True)

    class Meta:
        db_table = 'restuarant_food' 
        verbose_name = 'food'
        verbose_name_plural = 'foods'
        ordering = ["-id"]

    def __str__(self):
        return self.name