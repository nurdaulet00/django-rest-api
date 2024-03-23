from django.forms import model_to_dict
from rest_framework import generics, viewsets, mixins
from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .models import Cars, Category
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import CarsSerializer


class CarsAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    msx_page_size = 10000

#Возвращает список статей
class CarsAPIList(generics.ListCreateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = CarsAPIListPagination

#Изменяет запись
class CarsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAuthenticated, )
    #authentication_classes = (TokenAuthentication, )

#Удаляет запись
class CarsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Cars.objects.all()
    serializer_class = CarsSerializer
    permission_classes = (IsAdminOrReadOnly, )

















#class ViewSets!!
# class CarsViewSet(mixins.CreateModelMixin,
#                   mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   mixins.ListModelMixin,
#                   GenericViewSet):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer
#
#     @action(methods=['get'], detail=False) # Если будет Тру то будет одна запись, если Фолс то несколько
#     def category(self, request):
#         cats = Category.objects.all()
#         return Response({'cats': [c.name for c in cats]})

# class CarsAPIList(generics.ListCreateAPIView): # get and post
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer
#
# class CarsAPIUpdate(generics.UpdateAPIView): # Работает только с put and patch
#     queryset = Cars.objects.all() # Получает набор всех данных из таблицы "cars"
#     serializer_class = CarsSerializer
#
# class CarsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cars.objects.all()
#     serializer_class = CarsSerializer





# class CarsAPIView(APIView):
#     def get(self, request):
#         w = Cars.objects.all()
#         return Response({'posts': CarsSerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = CarsSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Cars.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = CarsSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         try:
#             instance = Cars.objects.get(pk=pk)
#             instance.delete()
#         except:
#             return Response({"ERROR": "Object Not Found!"})
#             return Response({"post":f"Object{str(pk)} is deleted"})

