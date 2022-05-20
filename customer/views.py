from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect


from .forms import AccountForm
from .models import Account, Customer


# Create your views here.
class LoginForm(View):
    def get(self, request):
        ac = AccountForm()
        return render(request, 'customer/login.html', {'ac': ac})
    def post(self, request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            if Account.objects.filter(username=username, password=password).exists():
                account=Account.objects.filter(username=username, password=password)
                customer = Customer.objects.get(pk=1)
                customerInfor = {
                    'lastname': customer.fullname.lastname,
                    'id': customer.id,
                }
                request.session['customerInfor'] = customerInfor
                return redirect('/')
            else:
                return redirect('/customer')