from django.shortcuts import render
from .forms import ExpenseForm

# Create your views here.


def HomeView(request):
    if request.method == "GET":
        form = ExpenseForm()
        return render(request, "expense/home.html", {"form": form})
