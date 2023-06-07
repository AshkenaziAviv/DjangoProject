from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields.related import ForeignKey
from django import forms

# Create your models here.
class Customer(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    log = models.BooleanField(default=False)
    items = models.CharField(max_length=100,default='')

    def __str__(self):
        return self.username

class Items(models.Model) :
    name = models.CharField(max_length=20,unique=True)  ###foreign key related to UserProfile.
    price = models.CharField(max_length=20,)            ## username of the friend.
    quantity_in_box = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    #class Meta:
     #   db_table = "Items"


class Orders(models.Model):
    sender=models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='sender') # to delete all the referenced
    description=models.CharField(max_length=50)
    duedate=models.DateField()
    date=models.DateField()
    cost =models.CharField(max_length=20,default=0)

    def __str__(self):
        return 'An order of '+str(self.sender) +' to the Baker.io in '+str(self.date)+' to '+str(self.duedate)

    #class Meta:
     #   db_table = "Orders"
class Items_in_order(models.Model):
    order_id=models.ForeignKey(Orders,on_delete=models.CASCADE,related_name='order_id')
    item_name=models.ForeignKey(Items,on_delete=models.CASCADE,related_name='item_name') # to delete all the referenced
    quantity_of_boxes=models.CharField(max_length=3)


