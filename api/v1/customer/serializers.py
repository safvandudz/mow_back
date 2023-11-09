from rest_framework.serializers import ModelSerializer
from customer.models import User,Customer
from restaurant.models import StoreCategory,Restaurant


# class LoginSerializer(ModelSerializer):
#      class Meta:
#         fields = ('id','number','password',)
#         model = User


# class  SignupSerializer(ModelSerializer):
#      class Meta:
#         fields = ('id', 'first_name', 'email', 'phone_nuuumber','password',)
#         model = User


class CategoriesSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name','image')
        model = StoreCategory


class RestaurantsSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name','image','category','tagline','rate')
        model = Restaurant


class FoodCategorySerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name','restaurant ','image')
        model = Restaurant


class FoodSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name','image','category','restaurant','PRICE')
        model = Restaurant

class AddressSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'door_number','street_address','city','landmark','pincode')
        model = Customer


        
class CartSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name','quantity','food','amount','image')
        model = Customer


class OrderSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'name','address','restaurant','amount','status')
        model = Customer











