# stock_app/controllers.py

from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .authentication import StaticTokenAuthentication
from .produit_repository import ProduitRepository
from .stock_service import StockService
from rest_framework import serializers
import logging

logger = logging.getLogger(__name__)

class ProduitResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    nom = serializers.CharField()
    prix = serializers.FloatField()
    categorie = serializers.IntegerField()

class ProduitRechercheView(APIView):
    authentication_classes = [StaticTokenAuthentication]

    def get(self, request):
        produit_id = request.query_params.get('id')
        nom = request.query_params.get('nom')
        categorie = request.query_params.get('categorie')

        criteria = {k: v for k, v in {
            'id': produit_id,
            'nom': nom,
            'categorie': categorie
        }.items() if v is not None}

        logger.info(f"🔍 Recherche produits: critères {criteria}")
        if not criteria:
            return Response(
                {"detail": "Fournir au moins un critère : id, nom ou categorie."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            stock_service = StockService(ProduitRepository())
            produits = stock_service.rechercher_produits(criteria)
            data = [model_to_dict(p) for p in produits]
            return Response(data, status=200)
        except Exception as e:
            logger.error(f"❌ Erreur recherche produit: {e}")
            return Response({"detail": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
