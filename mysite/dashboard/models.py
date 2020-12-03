from django.db import models

# Create your models here.

class Customer(models.Model):
    code = models.CharField(max_length=15)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    def __str__(self):
        return "{0} {1} {2}".format(self.code, self.name, self.phone)

class TotalMoneyCategory(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    drink = models.IntegerField()
    rice = models.IntegerField()
    spice = models.IntegerField()
    conv = models.IntegerField()
    fruit = models.IntegerField()
    other = models.IntegerField()
    nonfood = models.IntegerField()
    veget = models.IntegerField()
    meat = models.IntegerField()
    fish = models.IntegerField()
    tea = models.IntegerField()
    count = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12}".format(
            self.drink, self.rice, self.spice, self.conv, 
            self.fruit, self.other, self.nonfood, self.veget, self.meat,
            self.fish, self.tea, self.count, self.date
        )

class ClusterCenter(models.Model):
    drink = models.IntegerField()
    rice = models.IntegerField()
    spice = models.IntegerField()
    conv = models.IntegerField()
    fruit = models.IntegerField()
    other = models.IntegerField()
    nonfood = models.IntegerField()
    veget = models.IntegerField()
    meat = models.IntegerField()
    fish = models.IntegerField()
    tea = models.IntegerField()
    count = models.IntegerField()
    date = models.DateField()

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12}".format(
            self.drink, self.rice, self.spice, self.conv, 
            self.fruit, self.other, self.nonfood, self.veget, self.meat,
            self.fish, self.tea, self.count, self.date
        )

class ClusterCustomer(models.Model):
    cluster = models.ForeignKey(ClusterCenter, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1}".format(self.cluster, self.customer)