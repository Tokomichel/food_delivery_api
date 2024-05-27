from django.urls import path
from .views import Api_client, Api_livreur, Api_restaurant, Api_commande , Get_com

urlpatterns = [
    path('client', Api_client.as_view()),
    path('rest', Api_restaurant.as_view()),
    path('liv', Api_livreur.as_view()),
    path('com', Api_commande.as_view()),
    path('com/<str:nom>', Get_com.as_view()) # Get uniquement
]