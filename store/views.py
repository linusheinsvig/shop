from django.shortcuts import render

# Create your views here.

def store(request):
    """ A view to return the index page """

    return render(request, 'store/store.html')