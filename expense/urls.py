from django.conf.urls import url
from . import views

app_name = "expense"

urlpatterns = [
    url(
        r"home/$",
        views.HomeView,
        name="home",
    ),
]
