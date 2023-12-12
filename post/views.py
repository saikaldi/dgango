from django.shortcuts import HttpResponse, render, redirect
from django.conf import settings
from django.db.models import Q
from post.models import Product, Category, Review
from post.forms import ProductCreateForm, CetagoryCreateForm, ReviewCreateForm, ProductCreateForm2

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
        # settings.PAGE_SIZE

        print(request.user)
        products=Product.objects.all()

        search = request.GET.get('search')
        order = request.GET.get('order')

        if search:
            # products = products.filter(title__icontains=search) | products.filter(content__icontains=search)
            products = products.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )
        if order == 'title':
            products = products.order_by('title')
        elif order == '-title':
            products = products.order_by('-title')
        elif order == 'created_at':
            products = products.order_by('created_at')
        elif order == '-created_at':
            products = products.order_by('-created_at')

        max_page = products.__len__() / settings.PAGE_SIZE
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)
        

        page = int(request.GET.get('page', 1))
        start = (page - 1) * settings.PAGE_SIZE
        end = page * settings.PAGE_SIZE

        products = products[start:end]


        context={
                "products":products,
                "pages": range(1, max_page+1)
                 }

        return render(request, 'products/products.html', 
                      context=context)
    

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
def review_view(request):
    if request.method == 'GET':
        reviews=Review.objects.all()
        context={"reviews":reviews}
        return render(request, 'reviews/reviews.html', 
                      context=context)
 

def product_create(request):
    if request.method == 'GET':
        context = {
            "form":ProductCreateForm
        }
        return render(request, 'products/create.html', context )
    if request.method == 'POST':
        # print(request.POST)
        # print(request.FILES)
        # title=request.POST.get('title')
        # if not title:
        #     return HttpResponse("Title is required")
        
        # description=request.POST.get('description')
        # image=request.POST.get('image')
            form = ProductCreateForm(request.POST, request.FILES)
            if form.is_valid():
                # Product.objects.create(
                #     title=form.cleaned_data['title'],
                #     description=form.cleaned_data['description'],
                #     image=form.cleaned_data['image'],
                #     rate=form.cleaned_data['rate']
                    
                # )
                Product.objects.create(**form.cleaned_data)
                return redirect("/products/")
            context = {
            # "form":ProductCreateForm
            "form":form
        }
            return redirect('products/create.html', context)
    


def category_create(request):
    if request.method == 'GET':
        context = {
            "form":CetagoryCreateForm
        }
        return render(request, 'categories/create.html', context )
    if request.method == 'POST':
     
            form = CetagoryCreateForm(request.POST, request.FILES)
            if form.is_valid():
                # Category.objects.create(
                #     categoty_name=form.cleaned_data['categoty_name'],
                #     price_range=form.cleaned_data['price_range'],
                #     brand=form.cleaned_data['brand'],
                # )
                Category.objects.create(**form.cleaned_data)

                return redirect("/categories/")
            context = {
            "form":CetagoryCreateForm
        }
            return redirect('categories/create.html', context)
    



def reviews(request):
    if request.method == 'GET':
        context = {
            "form":ReviewCreateForm
        }
        return render(request, 'reviews/review.html', context )
    if request.method == 'POST':
     
            form = ReviewCreateForm(request.POST, request.FILES)
            if form.is_valid():
                Review.objects.create(**form.cleaned_data)
                # Review.objects.create(
                #     first_name=form.cleaned_data['first_name'],
                #     last_name=form.cleaned_data['last_name'],
                
                #     rate=form.cleaned_data['password'],
                #     review=form.cleaned_data['review'],
                # )
                return redirect("/reviews/")
            context = {
            "form":ReviewCreateForm
        }
            return redirect('reviews/review.html', context)
    
def product_update_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')
    
    if request.method == 'GET':
        context = {
            "form":ProductCreateForm2(instance=product)

        }
        return render(request, 'products/update.html', context)
    if request.method == 'POST':
        form = ProductCreateForm2(request.POST, request.FILES, instance=product)

        if form.is_valid():
            form.save()
            return redirect(f'/products/{product.id}/')

        return redirect(
            request,
            'products/update.html',
            {"form":form}
        )