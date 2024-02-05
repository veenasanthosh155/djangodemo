from django.shortcuts import render
from shop.models import Category,Product
from django.db.models import Q

def search(request):
    query = ""
    b = None
    if (request.method == "POST"):
        query = request.POST['q']
        if (query):
            b = Product.objects.filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request, 'search.html', {'query': query, 'b': b})

