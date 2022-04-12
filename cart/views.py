from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from book.models import BookItem

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

        html = render_to_string('cart/addcart.html', {'cart': cartInfo})
    return HttpResponse(html)

def shoppingcart(request):
    total = 0
    carts = request.session['cart']
    for key,value in carts.items():
        total+=int(value['price'])*int(value['num'])
    return render(request, 'cart/shoppingcart.html', {'total':total})