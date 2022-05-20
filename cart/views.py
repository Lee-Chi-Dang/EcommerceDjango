from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.shortcuts import redirect
from book.models import BookItem
from .forms import CartForm, OrderForm, PaymentForm
from .models import Order, Cart
from shipment.forms import ShipmentForm
from shipment.models import ShipmenCost, Shipment

# Create your views here.

cart = {}

def addcart(request):
    if request.is_ajax():
        id =request.POST.get('id')
        num = request.POST.get('num')

        bookItemCart = BookItem.objects.get(barcode=id)
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
    paymentForm = PaymentForm()
    return render(request, 'cart/shoppingcart.html', {'total':total, 'shipmentForm':shipmentForm, 'shipmentCost':shipmentCost, 'paymentForm':paymentForm})

def savecart(request):
    total = 0
    carts = request.session['cart']
    for key,value in carts.items():
        total+=int(value['price'])*int(value['num'])
    shipmentForm = ShipmentForm(request.POST)
    keyShipment = shipmentForm['selection'].value()
    addressShipment = shipmentForm['address'].value();
    shipmentCost = ShipmenCost.objects.get(id=keyShipment)
    total += shipmentCost.price
    #Shipment
    shipment = Shipment.objects.create(
        selection=keyShipment,
        address=addressShipment,
        codShip=shipmentCost
    )
    #End
    #Order
    order = Order.objects.create(
        status='Thanh cong',
        amount=total,
        shipment=shipment,
        customerId=1,
    )
    #End
    #Cart
    for key, value in carts.items():
        items = Cart.objects.create(
            proId=key,
            proPrice=value['price'],
            proImage=value['image'],
            proQuantity=value['num'],
            order=order,
        )
    #End
    paymentForm = PaymentForm(request.POST)
    keyPayment = paymentForm['type'].value()
    request.session.flush()
    return redirect('/cart/paypal')

def paypalPay(request):
    return render(request, 'cart/paypal.html')
