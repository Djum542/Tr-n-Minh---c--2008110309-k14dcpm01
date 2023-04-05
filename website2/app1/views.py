from django.shortcuts import render

# Create your views here.
def app(request):
    return render(request, 'app1/app1.html')
def app1(request):
    return render(request, 'app1/app1-2.html')