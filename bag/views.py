from django.shortcuts import render, redirect

# Create your views here.

def view_bag(request):
    """ A view to return the bag content page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add product to shopping bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    bag[item_id] = 1

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    if request.method == 'POST':
        # Perform the necessary logic to remove the item from the bag using the item_id
        bag = request.session.get('bag', {})
        if item_id in bag:
            del bag[item_id]
            request.session['bag'] = bag

        return redirect('view_bag')