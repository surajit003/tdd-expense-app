from django.conf.urls import url
from . import views

app_name = "expense"

urlpatterns = [
    url(r"home/$", views.HomeView, name="home"),
    url(
        r"^(?P<expense_id>[0-9a-f-]+)/detail/$",
        views.ExpenseDetail,
        name="expense_detail",
    ),
]
