from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.dateparse import parse_date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Customer, TotalMoneyCategory, ClusterCenter, ClusterCustomer
from sklearn.cluster import KMeans
import pandas as pd
import datetime

# Create your views here.

def _calculateTotalMoney(dataset):
    total = {"label":0, "drink":0, "rice":0, "spice":0, "conv":0, "fruit":0, "other":0, "nonfood":0, "veget":0, "meat":0, "fish":0, "tea":0}
    for row in dataset:
        total["drink"] += row["drink"]
        total["rice"] += row["rice"]
        total["spice"] += row["spice"]
        total["conv"] += row["conv"]
        total["fruit"] += row["fruit"]
        total["other"] += row["other"]
        total["nonfood"] += row["nonfood"]
        total["veget"] += row["veget"]
        total["meat"] += row["meat"]
        total["fish"] += row["fish"]
        total["tea"] += row["tea"]
    return total

def _calculatePercent(dataset):
    percent = {"label":0, "drink":0, "rice":0, "spice":0, "conv":0, "fruit":0, "other":0, "nonfood":0, "veget":0, "meat":0, "fish":0, "tea":0}
    totalMoney = 0
    for i in dataset.values():
        totalMoney += i
    percent["drink"] = round(dataset["drink"]*100/totalMoney, 2)
    percent["rice"] = round(dataset["rice"]*100/totalMoney, 2)
    percent["spice"] = round(dataset["spice"]*100/totalMoney, 2)
    percent["conv"] = round(dataset["conv"]*100/totalMoney, 2)
    percent["fruit"] = round(dataset["fruit"]*100/totalMoney, 2)
    percent["other"] = round(dataset["other"]*100/totalMoney, 2)
    percent["nonfood"] = round(dataset["nonfood"]*100/totalMoney, 2)
    percent["veget"] = round(dataset["veget"]*100/totalMoney, 2)
    percent["meat"] = round(dataset["meat"]*100/totalMoney, 2)
    percent["fish"] = round(dataset["fish"]*100/totalMoney, 2)
    percent["tea"] = round(dataset["tea"]*100/totalMoney, 2)
    return percent
    

def index(response):
    user = response.user
    if user.username == "":
        return HttpResponseRedirect("/login")
    last = ClusterCenter.objects.last()
    now = last.date
    pre = now - datetime.timedelta(days=1)
    pre = pre.replace(day=1)
    clusterNow = ClusterCenter.objects.filter(date=now)
    clusterPre = ClusterCenter.objects.filter(date=pre)
    monthNow = TotalMoneyCategory.objects.filter(date=now).values("drink", "rice", "spice", "conv", "fruit", "other", "nonfood", "veget", "meat", "fish", "tea")
    monthPre = TotalMoneyCategory.objects.filter(date=pre).values("drink", "rice", "spice", "conv", "fruit", "other", "nonfood", "veget", "meat", "fish", "tea")
    totalNow = _calculateTotalMoney(monthNow)
    totalPre = _calculateTotalMoney(monthPre)
    percentNow = _calculatePercent(totalNow)
    percentPre = _calculatePercent(totalPre)
    dictionary = {
        "username":user.username, 
        "clusterPre":clusterPre, 
        "clusterNow":clusterNow,
        "totalMoney":[totalPre, totalNow],
        "percent": [percentPre, percentNow],
        }
    return render(response, "desk/pages/index.html", dictionary)

def login(response):
    if response.method == "POST":
        username = response.POST.get("username")
        password = response.POST.get("password")
        user = authenticate(response, username=username, password=password)
        if user:
            auth_login(response, user)
            return HttpResponseRedirect("/")
        else:
            error = "Login fails !"
            return render(response, "desk/pages/login.html", {"error":error})
    else:
        return render(response, "desk/pages/login.html", {"error":""})

def logout(response):
    auth_logout(response)
    return HttpResponseRedirect("/login")

def register(response):
    if response.method == "POST":
        firstname = response.POST.get("firstname")
        lastname = response.POST.get("lastname")
        username = response.POST.get("username")
        password = response.POST.get("password")
        confirm = response.POST.get("confirm")
        if password != "" and password == confirm:
            try:
                user = User.objects.get(username=username)
                error = "User existed !"
                return render(response, "desk/pages/register.html", {"error":error})
            except:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, password=password, is_staff=True)
                user.save()
                return HttpResponseRedirect("/")
        else:
            error = "Register fails !"
            return render(response, "desk/pages/register.html", {"error":error})
    else:
        return render(response, "desk/pages/register.html", {"error":""})
    
def password(response):
    return render(response, "desk/pages/password.html")


def _importCustomer(filepath):
    data = pd.read_csv(filepath)
    data = data.values
    for item in data:
        code = item[0]
        name = item[1]
        phone = item[2]
        row = Customer(code=code, name=name, phone=phone)
        row.save()

def _importTotalMoney(filepath):
    data = pd.read_csv(filepath)
    data = data.values
    for item in data:
        customer = Customer.objects.get(code=item[0])
        drink = item[1]
        rice = item[2]
        spice = item[3]
        conv = item[4]
        fruit = item[5]
        other = item[6]
        nonfood = item[7]
        veget = item[8]
        meat = item[9]
        fish = item[10]
        tea = item[11]
        count = item[12]
        date = item[13] + "-1"
        row = customer.totalmoneycategory_set.create(drink=drink, rice=rice, spice=spice, conv=conv, fruit=fruit, other=other, nonfood=nonfood, veget=veget, meat=meat, fish=fish, tea=tea, count=count, date=date)
        row.save()

def _importClusterCenter(data):
    center = data["center"]
    detail = data["detail"]
    date = data["date"]
    for i in range(len(center)):
        item = center[i]
        drink = item[0]
        rice = item[1]
        spice = item[2]
        conv = item[3]
        fruit = item[4]
        other = item[5]
        nonfood = item[6]
        veget = item[7]
        meat = item[8]
        fish = item[9]
        tea = item[10]
        count = item[11]
        date = date
        rowcen = ClusterCenter(drink=drink, rice=rice, spice=spice, conv=conv, fruit=fruit, other=other, nonfood=nonfood, veget=veget, meat=meat, fish=fish, tea=tea, count=count, date=date)
        rowcen.save()
        for code in detail[i]:
            cus = Customer.objects.get(code=code)
            rowcus = rowcen.clustercustomer_set.create(customer=cus)
            rowcus.save()

def _train(filepath):
    csv = pd.read_csv(filepath)
    data = csv.values
    train = data[:, 1:13]
    customer = data[:, 0]
    date = data[0,13] + "-1"
    kmeans = KMeans(n_clusters=5, random_state=0).fit(train)
    center = kmeans.cluster_centers_
    label = kmeans.labels_
    detail = [[],[],[],[],[]]
    for i in range(len(label)):
        detail[label[i]].append(customer[i])
    return {"center":center, "detail":detail, "date":date}

def _cluster(filepath):
    data = _train(filepath)
    _importClusterCenter(data)


def showChart(response):
    user = response.user
    if user.username == "":
        return HttpResponseRedirect("/login")
    if response.method == "POST":
        if response.POST.get("pickDate") != None and response.POST.get("dateValue") != "":
            date = response.POST.get("dateValue")
            data = ClusterCenter.objects.filter(date=date)
            return render(response, "desk/pages/views.chart.html", {"data":data, "date":date, "username":user.username})
    last = ClusterCenter.objects.last()
    date = str(last.date)
    data = ClusterCenter.objects.filter(date=date)
    return render(response, "desk/pages/views.chart.html", {"data":data, "date":date, "username":user.username})

def showDetail(response, id):
    user = response.user
    if user.username == "":
        return HttpResponseRedirect("/login")
    center = ClusterCenter.objects.get(id=id)
    data = center.clustercustomer_set.all()
    return render(response, "desk/pages/views.detail.html", {"data":data, "username":user.username})

def showCustomer(response):
    user = response.user
    if user.username == "":
        return HttpResponseRedirect("/login")
    data = Customer.objects.all()
    return render(response, "desk/pages/tables.customer.html", {"data":data, "username":user.username})

def showTotalMoney(response):
    user = response.user
    if user.username == "":
        return HttpResponseRedirect("/login")
    if response.method == "POST":
        if response.POST.get("pickDate") != None and response.POST.get("dateValue") != "":
            date = response.POST.get("dateValue")
            data = TotalMoneyCategory.objects.filter(date=date)
            return render(response, "desk/pages/tables.totalmoney.html", {"data":data, "date":date, "username":user.username})
    last = TotalMoneyCategory.objects.last()
    date = str(last.date)
    data = TotalMoneyCategory.objects.filter(date=date)
    return render(response, "desk/pages/tables.totalmoney.html", {"data":data, "date":date, "username":user.username})

def importCustomer(response):
    user = response.user
    if user.username == "":
        return HttpResponseRedirect("/login")
    customerPath = "Choose files"
    message = None
    if response.method == "POST":
        base = "./dashboard/static/datatable/"
        if response.POST.get("importCustomer") != None:
            filename = response.POST.get("fileCustomer")
            if filename != "":
                customerPath = base + filename
                _importCustomer(customerPath)
                message =  "Import file successfuly !"
                return render(response, "desk/pages/imports.customer.html", {"message":message, "customerPath":customerPath, "username":user.username})
    return render(response, "desk/pages/imports.customer.html", {"message":message, "customerPath":customerPath, "username":user.username})

def importTotalMoney(response):
    user = response.user
    if user.username == "":
        return HttpResponseRedirect("/login")
    totalMoneyPath = "Choose files"
    message = None
    if response.method == "POST":
        base = "./dashboard/static/datatable/"
        if response.POST.get("importTotalMoney") != None:
            filename = response.POST.get("fileTotalMoney")
            if filename != "":
                totalMoneyPath = base + filename
                _importTotalMoney(totalMoneyPath)
                _cluster(totalMoneyPath)
                message =  "Import file successfuly !"
                return render(response, "desk/pages/imports.totalmoney.html", {"message":message, "totalMoneyPath":totalMoneyPath, "username":user.username})
    return render(response, "desk/pages/imports.totalmoney.html", {"message":message, "totalMoneyPath":totalMoneyPath, "username":user.username})


# End of file