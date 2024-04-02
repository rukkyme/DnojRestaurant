from django.urls import path
from . import views


urlpatterns = [
    path('menu-items', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemsView.as_view()), #<int:pk> specifies that an integer value will follow menu-items/, 
    #and it will be captured as the primary key of the menu item.
    
]
