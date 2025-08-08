from django.urls import path
from .controllers import ProduitRechercheView

urlpatterns = [
    # path('ping/', ping),
    path('stockService/recherche/', ProduitRechercheView.as_view(), name='produit-recherche'),
]