from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.http import HttpResponseNotFound


# Create your views here.


def HomeView(request):
    if request.method == "GET":
        form = ExpenseForm()
        return render(request, "expense/home.html", {"form": form})
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            instance = form.save()
            return redirect("expense:expense_detail", expense_id=instance.expense_id)
        return render(request, "expense/home.html", {"form": form})


def ExpenseDetail(request, expense_id):
    if request.method == "GET":
        expense = Expense.objects.filter(expense_id=expense_id)
        if expense:
            return render(request, "expense/detail.html", {"expense": expense})
        else:
            return HttpResponseNotFound("No expense found with those details")
