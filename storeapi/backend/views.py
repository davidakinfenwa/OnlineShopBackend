from django.shortcuts import render
from django.core.mail import send_mail
from storeapi.settings import EMAIL_HOST_USER

from .models import Order
from .serializers import OrderSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination    


# Create your views here.

def get_paginated_queryset_response(qs,request):
        pagination=PageNumberPagination()
        pagination.page_size=2
        paginated_qs=pagination.paginate_queryset(qs,request)
        serializers = OrderSerializer(paginated_qs, many=True)
        return pagination.get_paginated_response(  {'message': 'Order Fetch Succesully','data': serializers.data, })
class OrderView(APIView):
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)
            return get_paginated_queryset_response(orders, request)
        except Exception as e:
            print(e)
            return Response({'data': serializer.error_messages, 'message': 'Expection Found While fetching'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = OrderSerializer(data=data)
            if not serializer.is_valid():
                return Response({'data': serializer.errors, 'message': 'Somthing went wrong when posting data'}, status=status.HTTP_400_BAD_REQUEST)
            subject = "New Order Has been created"
            message = "Dear David Test again"
            email=data['customeremail']
            print(EMAIL_HOST_USER)
            recipient_list = [email]
            send_mail(subject, message, EMAIL_HOST_USER,
                      recipient_list, fail_silently=True)
            
            serializer.save()
            return Response({'data': serializer.data, 'message': 'Order Created Successfully'}, status=status.HTTP_201_CREATED)
        except  Exception as e:
            print(e)
            return Response({'data': {}, 'message': 'Exception- Something went wrong in creation of data'}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        try:
            data = request.data
            order1 = Order.objects.filter(id=data.get('id'))

            if not order1.exists():
                return Response({'data': {}, 'message': 'Order Not Found'}, status=status.HTTP_404_NOT_FOUND)
            obj = order1.first()
            serializer = OrderSerializer(obj, data=data, partial=True)
            print(serializer.is_valid())
            if serializer.is_valid():
                serializer.save()
                return Response({'data': serializer.data}, status=status.HTTP_200_OK or status.HTTP_201_CREATED)
            return Response({'data': {}, 'message': 'Somthing went wrong when posting data'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            return Response({'data': {}, 'message': 'Data Not Found While fetching'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        try:
            data=request.data
            qs = Order.objects.filter(id=data.get('id'))
            if not qs.exists():
                return Response({'data': {}, 'message': 'Order Not Found'}, status=status.HTTP_404_NOT_FOUND)
            obj = qs.first()
            obj.delete()
            return Response({'data': {}, 'message': 'Order Deleted Successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'data': e, 'message': 'Exception- Something went wrong in deletion of data'}, status=status.HTTP_400_BAD_REQUEST)
