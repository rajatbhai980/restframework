from django.urls import path, include
from .views import *

urlpatterns = [
   path("", ApiOverview, name='home'), 
   path("add_item/", add_item, name='create'), 
   path("view_item/", view_item, name="read"), 
   path("update_item/<int:pk>/", update_item, name="update"), 
   path("delete_item/<int:pk>/", delete_item, name="delete"), 

]