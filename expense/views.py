from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.http import HttpResponseNotFound, HttpResponse
from django.db import IntegrityError
from datetime import datetime
from .utils import render_to_pdf

now = datetime.now().strftime("%Y-%m")


# Create your views here.


def HomeView(request):
    if request.method == "GET":
        form = ExpenseForm()
        return render(request, "expense/home.html", {"form": form})
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            try:
                instance = form.save()
            except IntegrityError as ex:
                yr, mon = now.split("-")
                expense = Expense.objects.get(month=mon, year=yr)
                return render(
                    request,
                    "expense/home.html",
                    {"form": form, "expense_id": expense.expense_id},
                )
            else:
                return redirect(
                    "expense:expense_detail", expense_id=instance.expense_id
                )
        return render(request, "expense/home.html", {"form": form})


def ExpenseDetail(request, expense_id):
    if request.method == "GET":
        try:
            exp = Expense.objects.get(expense_id=expense_id)
            pdf = render_to_pdf("expense/expense_pdf.html", exp.__dict__)
            return HttpResponse(pdf, content_type="application/pdf")
        except Expense.DoesNotExist:
            return HttpResponseNotFound("No expense found with those details")
