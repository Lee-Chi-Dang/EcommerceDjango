from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from book.models import BookItem
from .forms import CartForm, OrderForm
from .models import Order, Cart
from shipment.forms import ShipmentForm
from shipment.models import ShipmenCost

# Create your views here.

cart = {}

def addcart(request):
    if request.is_ajax():
        id =request.POST.get('id')
        num = request.POST.get('num')

        bookItemCart = BookItem.objects.get(barcode = id)
        if id in cart.keys():
            itemCart = {
                'name': bookItemCart.book.title,
                'price': bookItemCart.price,
                'image': bookItemCart.book.image,
                'num': int(cart[id]['num'])+1
            }
        else:
            itemCart = {
                'name': bookItemCart.book.title,
                'price': bookItemCart.price,
                'image': bookItemCart.book.image,
                'num': num
            }
        cart[id] = itemCart
        request.session['cart'] = cart
        cartInfo = request.session['cart']

        # html = render_to_string('cart/addcart.html', {'cart': cartInfo})
    return render(request,'cart/addcart.html', {'cart': cartInfo})

def shoppingcart(request):
    total = 0
    carts = request.session['cart']
    for key,value in carts.items():
        total+=int(value['price'])*int(value['num'])
    shipmentForm = ShipmentForm()
    shipmentCost  = ShipmenCost.objects.all()
    return render(request, 'cart/shoppingcart.html', {'total':total, 'shipmentForm':shipmentForm, 'shipmentCost':shipmentCost})

def savecart(request):
    total = 0
    carts = request.session['cart']
    for key,value in carts.items():
        total+=int(value['price'])*int(value['num'])
    shipmentForm = ShipmentForm(request.POST)
    keyShipment = shipmentForm['selection'].value()
    shipmentCost = ShipmenCost.objects.get(id=keyShipment)
    total += shipmentCost.price
    #Order
    order = Order.objects.create(
        status='Thanh cong',
        amount=total,
        shipment=shipmentForm
    )
    #End
    #Cart
    for key, value in carts.items():
        items = Cart.objects.create(
            orderId=order,
            order_no='ORDER_'+str(order.id),
            proId=key,
            proPrice=value['price'],
            proImage=value['image'],
            proQuantity=value['num'],
        )
    #End
    return  HttpResponse('Thanh cong' +str(total))

