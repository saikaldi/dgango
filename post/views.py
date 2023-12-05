from django.shortcuts import HttpResponse, render
from post.models import Product, Category
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
    product=Product.objects.all()
    categories=Category.objects.all()
    print(categories)
    for c in categories:
        print(c.name)
    if request.method == 'GET':

        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products=Product.objects.all()
        
        return render(request, 'products/products.html', 
                      context={"products":products})
    

def product_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            product=Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'errors/404.html')
        # print(product)

        
        context={
            'product':product
        }
        return render(request,'products/details.html', context)
        # return HttpResponse(f"{product_id}")
    
def category_view(request):
    if request.method == 'GET':
        categories=Category.objects.all()
        context={"categories":categories}
        return render(request, 'products/categories.html', 
                      context=context)
 