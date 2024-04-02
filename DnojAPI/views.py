from rest_framework import generics
from .models import MenuItem
from .serializers import MenuItemSerializer
#from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    '''
    @swagger_auto_schema(operation_summary="List all menu items")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Create a new menu item")
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
'''
    
# this will display a single menu item at a time.
# the RetrieveUpdateView class has everything to fetch a record, 
# display it, and accept post calls to update them
# DestroyApiView, has everything to accept, delete calls, and 
# finally, delete a record
class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    '''
    @swagger_auto_schema(operation_summary="Retrieve a menu item")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Update a menu item")
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(operation_summary="Delete a menu item")
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    '''