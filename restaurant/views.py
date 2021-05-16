from django.http import response
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializers import MenuSerializer, OrderSerializer, TableSerializer , TableBookingSerializer
from .models import Menu, Order , Table, TableBooking
from rest_framework import status
from rest_framework.response import Response
from . import models, serializers
from rest_framework.decorators import api_view
from django.db.models import Avg, Count, Min, Sum , Max



class ViewMenu(ListAPIView): 
    """This endpoint list all of the available todos from the database""" 
    queryset = Menu.objects.all() 
    serializer_class = MenuSerializer

@api_view(['GET','POST'])
def take_order(request):
    if request.method == 'GET':
        serializer = MenuSerializer(Menu.objects.all(), many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            result =generate_bill(request.data["items"])
            resp= {"Congratulations! your order is placed. Total bill is": result[0],
                    "Your order will be prepared in Minutes-" :result[1],
                    "Table Number": request.data["table_no"]}
            return Response(resp , status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def generate_bill(list1):
    bill = Menu.objects.filter(id__in = list1).aggregate(bill_price=Sum("price"))
    time = Menu.objects.filter(id__in=list1).aggregate(time_to_prepare = Max("time_to_prepare"))
    answer =[bill["bill_price"],time["time_to_prepare"]]
    return answer

@api_view(['GET','POST'])
def book_table(request):
    if request.method == 'GET':
        return Response({"Welcome to table booking API"})
        

    if request.method == 'POST':
        serializer = TableBookingSerializer(data=request.data)
        if serializer.is_valid():
            available_table= Table.objects.filter(pk=1).values("available_table")
            if (available_table[0]['available_table']>0):
                Table.objects.filter(pk=1).update(available_table =available_table[0]["available_table"] - 1)
                Table.objects.filter(pk=1).update(booked_table =Table.objects.filter(pk=1).values("booked_table")[0]['booked_table'] + 1)
                serializer.save()
                table_no = "TB00"+str(TableBooking.objects.filter(name=request.data["name"]).values("id")[0]['id'])
                resp= {"Congratulations! your Table for is booked. table number is": table_no,
                        "Table for" : request.data["people"]}
                return Response(resp , status=status.HTTP_201_CREATED)
            else:
                resp= {"Sorry!, currently all tables are booked"}
                return Response(resp , status=status.HTTP_201_CREATED)
                

class TableDetails(ListAPIView): 
    queryset = Table.objects.all() 
    serializer_class = TableSerializer

