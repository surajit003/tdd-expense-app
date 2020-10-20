from django.shortcuts import render
from .forms import ExpenseForm

# Create your views here.


def HomeView(request):
    if request.method == "GET":
        form = ExpenseForm()
        return render(request, "expense/home.html", {"form": form})
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "expense/home.html", {"form": form})
