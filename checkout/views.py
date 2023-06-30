from django.shortcuts import render
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)
