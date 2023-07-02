from django.shortcuts import render, redirect
from django.conf import settings
import stripe
from .forms import OrderForm
from bag.contexts import bag_contents


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    bag = request.session.get('bag', {})
    
    current_bag = bag_contents(request)
    total = current_bag['total']
    
    if total <= 0:
        return render(request, 'checkout/error.html', {'error_message': 'Total must be greater than zero.'})
    
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    
    try:
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        print(intent)
        
        order_form = OrderForm()
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }
        
        return render(request, template, context)
    
    except stripe.error.InvalidRequestError as e:
        print(f"Stripe Error: {str(e)}")
        return render(request, 'checkout/error.html', {'error_message': 'An error occurred during payment processing.'})