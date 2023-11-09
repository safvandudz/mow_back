from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status

from django.contrib.auth import authenticate
from .serializers import CategoriesSerializer,RestaurantsSerializer,FoodCategorySerializer,FoodSerializer,CartSerializer,OrderSerializer,AddressSerializer
from user.models import User
from customer.models import Customer,Cart,Order,Address
from restaurant.models import StoreCategory,Restaurant,Food,FoodCategory



@api_view(["POST"])
@permission_classes ([AllowAny])
def login(request):
    phone_number=request.data.get('phone_number')
    password=request.data.get('password')

    if User.objects.filter(phone_number=phone_number).exists():
        user = authenticate(request, phone_number=phone_number, password=password)

        if user is not None:

            if Customer.objects.filter(user=user).exists():

                refresh = RefreshToken.for_user(user)

                response_data = {
                    "status_code" : 6000,
                    "data": {
                        "id": user.id,
                        "pnone_number": user.phone_number,
                        'access': str(refresh.access_token),
                    },
                    "message": "Successfully logged in"
                }
            else:
                response_data = {
                    "status_code" : 6001,
                    "data": {
                        "message": "Invalid phone number or password",
                        "phone_number":phone_number,
                    },
                }

        else:
            response_data = {
                "status_code" : 6001,
                "data": {
                    "message": "Invalid password",
                    "phone_number":phone_number,
                },
            }

    else:
        response_data = {
            "status_code" : 6001,
            "data": {
                "message": "Not registered phone number",
                "phone_number":phone_number,
            },
        }

    return Response(response_data)


@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    name = request.data.get("name")
    email = request.data.get("email")
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')


    if User.objects.filter(phone_number=phone_number).exists():
        response_data = {
            "status_code": 6001,
            "data": {
                "message": "Phone number is already registered",
                "phone_number": phone_number,
            },
        }
        

    else:

        user = User.objects.create_user(phone_number=phone_number, password=password,email=email, first_name=name, is_customer=True)

        customer = Customer.objects.create(user=user)

        customer.save()

        refresh = RefreshToken.for_user(user)
        
        response_data = {
            "status_code": 6000,
            "data": {
                "id": user.id,
                "phone_number": user.phone_number,
                'access': str(refresh.access_token),
            },
            "message": "User registered successfully",
        }
    
    return Response(response_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def categories(request):
    
    categories= StoreCategory.objects.all()
    context = {
        "request": request
    }

    serializer = CategoriesSerializer(categories, many=True,context=context)
    response_data = {
        "status_code": 6001,
        "data": serializer.data,
    }
    return Response(response_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def restaurants(request): 
    
    restaurants= Restaurant.objects.all()
    q = request.GET.get('q')
    if q:
        category = StoreCategory.objects.get(id=q)
        restaurants = restaurants.filter(category=category)


    context = {
        "request": request
    }

    serializer = RestaurantsSerializer(restaurants, many=True,context=context)
    response_data = {
        "status_code": 6001,
        "data": serializer.data,
    }
    return Response(response_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def food_category(request, id):
    
    restaurant = Restaurant.objects.get(id=id)
    food_categories= FoodCategory.objects.filter(restaurant=restaurant)

    context = {
        "request": request
    }

    serializer = FoodCategorySerializer(food_categories, many=True,context=context)
    response_data = {
        "status_code": 6001,
        "data": serializer.data,
    }
    return Response(response_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def foods(request,id):

    restaurant = Restaurant.objects.get(id=id)
    foods= Food.objects.filter(restaurant=restaurant)
    r = request.GET.get('r')
    if r:
        category = FoodCategory.objects.get(id=r)
        foods = foods.filter(category=category)

    context = {
        "request": request
    }

    serializer = FoodSerializer(foods, many=True,context=context)
    response_data = {
        "status_code": 6001,
        "data": serializer.data,
    }
    return Response(response_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart(request):
    user=request.user
    customer = Customer.objects.get(user=user)
    
    cart= Cart.objects.filter(is_ordered=False,customer=customer)
    context = {
        "request": request
    }

    serializer = CartSerializer(cart, many=True,context=context)
    response_data = {
        "status_code": 6001,
        "data": serializer.data,
    }
    return Response(response_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def address(request):
    user=request.user
    customer = Customer.objects.get(user=user)
    
    address= Address.objects.filter(customer=customer)
    context = {
        "request": request
    }

    serializer = AddressSerializer(address, many=True,context=context)
    response_data = {
        "status_code": 6001,
        "data": serializer.data,
    }
    return Response(response_data)







@api_view(['GET'])
@permission_classes([IsAuthenticated])
def orders(request):
    user=request.user
    customer = Customer.objects.get(user=user)
    
    order= Order.objects.filter(customer=customer)

    context = {
        "request": request
    }

    serializer = OrderSerializer(order, many=True,context=context)
    response_data = {
        "status_code": 6001,
        "data": serializer.data,
    }
    return Response(response_data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cart_add(request):
    user = request.user
    customer = Customer.objects.get(user=user)

    food = request.data.get('food')
    food = Food.objects.get(id=food)

    if food is not None:
        cart = Cart.objects.create(
            customer=customer,
            food=food,
            quantity=1,
            amount=food.price
        )
        cart.save()

        response_data = {
            "status_code": 6001,
            "message": "successfully added",
        }
    return Response(response_data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cart_plus(request):
    user = request.user
    customer = Customer.objects.get(user=user)

    id = request.data.get('id')

    try:
        cart_item = Cart.objects.get(customer=customer, id=id, is_ordered=False)
    except Cart.DoesNotExist:
        return Response({"error": "Cart item not found."}, status=404)

    
    cart_item.quantity += 1
    cart_item.save()

    serializer = CartSerializer(cart_item, context={"request": request})

    response_data = {
        "status_code": 6001,
        "data": serializer.data,
        "message": "Quantity incremented successfully.",
    }

    return Response(response_data)

def cart_minus(request):
    user = request.user
    customer = Customer.objects.get(user=user)

    id = request.data.get('id')

    try:
        cart_item = Cart.objects.get(customer=customer, id=id, is_ordered=False)
    except Cart.DoesNotExist:
        return Response({"error": "Cart item not found."}, status=404)

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        return Response({"error": "Quantity cannot be less than 1."}, status=400)

    serializer = CartSerializer(cart_item, context={"request": request})

    response_data = {
        "status_code": 6002,
        "data": serializer.data,
        "message": "Quantity decremented successfully.",
    }

    return Response(response_data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_order(request):
    user = request.user
    customer = Customer.objects.get(user=user)
    cart_items = request.data.get('cart_items')  
    quantities = request.data.get('quantities')  
 

    total_amount = 0
    for i,id in enumerate(cart_items):
        cart_items = cart_items.objects.get(id=id)
        total_amount += cart_items.price * quantities[i]

    order = Order.objects.create(customer=customer, total_amount=total_amount, is_ordered=True)

    for i, id in enumerate(cart_items):
        cart_items = cart_items.objects.get(id=id)
        order.cart_items.add(cart_items)
        order.quantities.add(quantities[i])

    order.save()

    serializer = OrderSerializer(order, context={"request": request})

    response_data = {
        "status_code": 6002,
        "data": serializer.data,
        "message": "Order placed successfully.",
    }

    return Response(response_data)
