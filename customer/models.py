from django.db import models
from user.models import User
from restaurant.models import Food,Restaurant
class Customer(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)



    class Meta:
        db_table = 'customer_customer' 
        verbose_name = 'customer'
        verbose_name_plural = 'customers'
        ordering = ["-id"]

    def __str__(self):
        return self.user.phone_number



class Address(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    door_number=models.CharField(max_length=100)
    street_address=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    landmark=models.CharField(max_length=100)
    pincode=models.IntegerField(blank=True,null=True)

    class Meta:
        db_table = 'customer_address' 
        verbose_name = 'address'
        verbose_name_plural = 'addresss'
        ordering = ["-id"]

    def __str__(self):
        return self.customer
    
class Cart(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    food=models.ForeignKey(Food,on_delete=models.CASCADE)
    quantity=models.IntegerField(blank=True,null=True)
    amount=models.IntegerField()
    is_ordered=models.BooleanField(default=False)

    class Meta:
        db_table = 'customer_cart' 
        verbose_name = 'cart'
        verbose_name_plural = 'carts'
        ordering = ["-id"]

    def __str__(self):
        return self.customer
    
class Order(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    restaurant=models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    cart_items=models.ForeignKey(Food,on_delete=models.CASCADE)
    amount=models.IntegerField()
    status=models.CharField(max_length=100)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    


    class Meta:
        db_table = 'customer_order' 
        verbose_name = 'order'
        verbose_name_plural = 'orders'
        ordering = ["-id"]

    def __str__(self):
        return self.customer
    

class Feedback(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    order=models.ForeignKey(Order,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.CharField(max_length=1000)
    # star=



    class Meta:
        db_table = 'customer_feed_back' 
        verbose_name = 'feedback'
        verbose_name_plural = 'feedbacks'
        ordering = ["-id"]

    def __str__(self):
        return self.customer