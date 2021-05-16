from django.db import models
from django.db.models.deletion import CASCADE

class Menu(models.Model):
    # id = models.IntegerField(null=False, unique=True, primary_key=True)
    items=models.CharField(null=False, max_length=100)
    price=models.IntegerField(null=False)
    time_to_prepare = models.IntegerField(null=False)
    

    def __str__(self):
        return self.items


class TableBooking(models.Model):
    # id = models.IntegerField(null=False, unique=True, primary_key=True)
    name = models.CharField(null=False, max_length=100)
    people = models.IntegerField(null=False)

    def __str__(self):
        return self.name

class Order(models.Model):
    # id = models.IntegerField(null=False, unique=True, primary_key=True)
    items = models.ManyToManyField(Menu)
    table_no = models.ForeignKey(TableBooking , on_delete=models.CASCADE )
    # quantity = models.JSONField()


class Table(models.Model):
    # id = models.IntegerField(null=False, unique=True, primary_key=True)
    total_table = models.IntegerField(null=False)
    booked_table = models.IntegerField(null=True)
    available_table = models.IntegerField(null=True)

    def __int__(self):
        return self.id


