from django.shortcuts import render
from django.conf import settings
from .forms import OrderForm
from bag.contexts import bag_contents


def checkout(request):
    bag = request.session.get('bag', {})
    
    current_bag = bag_contents(request)
    total = current_bag['total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51NNFEzChlBYEIuSVgX3DT2BiKOEp38EOS03eFWuijU6XwsQ0F6Fc9C3GxgKABY7LxE38y5aY0Yd7sqnNIamjefiW00s5aJpn9T',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
