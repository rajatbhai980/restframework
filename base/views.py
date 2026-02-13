from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import  Item
from .serializers import ItemSerializer
from rest_framework import viewsets, serializers, status 
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def ApiOverview(request): 
    urls = {
        'all_items': '/',
        'Search by Category': '/?category=/categoryname', 
        'Search by SubCategory': '/?sub_category=/subcategoryname', 
        'Add': '/create', 
        'Update': '/update/pk', 
        'Delete': '/item/pk/delete' 
    }

    return Response(urls)

@api_view(['POST'])
def add_item(request): 
    item = ItemSerializer(data=request.data)

    if Item.objects.filter(**request.data).exists(): 
        raise serializers.ValidationError('This data already exists')
    
    if item.is_valid(): 
        item.save()
        return Response(item.data)
    else: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def view_item(request):
    if request.query_params:  
        item = Item.objects.filter(**request.query_params.dict())
    else: 
        item = Item.objects.all()

    if item: 
        return_data = ItemSerializer(item, many=True)
        return Response(return_data.data)
    else: 
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def update_item(request, pk): 
    item = Item.objects.get(pk=pk)
    item_ser = ItemSerializer(instance=item, data=request.data)

    if item_ser.is_valid(): 
        item_ser.save()
        return Response(item_ser.data)
    else: 
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_item(request, pk): 
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return Response(status=status.HTTP_202_ACCEPTED)
