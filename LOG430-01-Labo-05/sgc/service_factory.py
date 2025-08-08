from sgc.core.services.transaction_manager import TransactionManager
from sgc.microservices.stock_service.stock_app.stock_service import StockService
from sgc.microservices.vente_service.vente_app.vente_service import VenteService
from sgc.caisse.services.caisse_service import CaisseService

# Un seul transaction manager global (pas de cursor ici)
transaction_manager = TransactionManager()

# Factory principale
def get_caisse_service():
    with transaction_manager.atomic():
        # Réinstancier les repositories à chaque appel avec un cursor actif
        from sgc.microservices.stock_service.repositories.produit_repository import ProduitRepository
        from sgc.microservices.vente_service.repositories.vente_repository import VenteRepository

        produit_repository = ProduitRepository()
        vente_repository = VenteRepository()

        stock_service = StockService(produit_repository)
        vente_service = VenteService(vente_repository, stock_service)
        caisse_service = CaisseService(transaction_manager, stock_service, vente_service)

        return caisse_service
