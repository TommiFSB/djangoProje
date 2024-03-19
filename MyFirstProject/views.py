from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello Word!</h1>")
def first_page(request):
    return render(request,'1.html')
def second_page(request):
    return render(request,'2.html')
def three_page(request):
    return render(request,'3.html')
def four_page(request):
    return render(request,'4.html')
def fife_page(request):
    return render(request,'5.html')