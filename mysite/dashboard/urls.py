from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("register/", views.register, name="register"),
    path("password/", views.password, name="password"),
    path("views/chart/", views.showChart, name="views.chart"),
    path("views/detail/<int:id>", views.showDetail, name="views.detail"),
    path("tables/customer/", views.showCustomer, name="tables.customer"),
    path("tables/total-money/", views.showTotalMoney, name="tables.totalmoney"),
    path("imports/customer/", views.importCustomer, name="imports.customer"),
    path("imports/total-money/", views.importTotalMoney, name="imports.totalmoney"),
]