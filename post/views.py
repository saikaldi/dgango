from django.shortcuts import HttpResponse, render
# from datetime import datetime
# current_date=datetime.now()
# Create your views here.
def hello_view(request):
    return HttpResponse('Hello! Its my project')
def current_date_view(request):
    return HttpResponse("Current date: 16.11.2023")
def goodbye_view(request):
    return HttpResponse('Goodbye user!')
def goodmorning_view(request):
    return render(request, 'index.html')




