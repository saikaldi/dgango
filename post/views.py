from django.shortcuts import HttpResponse, render
from post.models import Product
# from datetime import datetime
# current_date=datetime.now()
# Create your views here.
# Lesson 1
# def hello_view(request):
#     return HttpResponse('Hello! Its my project')
# def current_date_view(request):
#     return HttpResponse("Current date: 16.11.2023")
# def goodbye_view(request): n
#     return HttpResponse('Go2odbye user!')
# def goodmorning_view(request):
#     return render(request, 'index.html')

# Lesson 2
def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products=Product.objects.all()
        return render(request, 'products/products.html', 
                      context={"products":products})

