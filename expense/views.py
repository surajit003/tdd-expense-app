from django.shortcuts import render

# Create your views here.

def HomeView(request):
    if request.method=='GET':
        return render(request,'expense/home.html')