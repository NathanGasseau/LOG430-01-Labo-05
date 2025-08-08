from ..models import (
    Categorie, Produit, StockProduit
)

def run():
    if Categorie.objects.exists() or Produit.objects.exists():
        print("✅ Données déjà présentes, aucun seed nécessaire.")
        return

    print("🌱 Insertion des données de départ...")
    if Categorie.objects.exists() or Produit.objects.exists():
        return  # Évite de dupliquer les données à chaque démarrage

    # Création de catégories
    cat_elec = Categorie.objects.create(nom="Électronique", description="Produits électroniques")
    cat_bureau = Categorie.objects.create(nom="Bureau", description="Fournitures de bureau")

    # Création de produits
    clavier = Produit.objects.create(nom="Clavier mécanique", categorie=cat_elec, prix=120)
    souris = Produit.objects.create(nom="Souris sans fil", categorie=cat_elec, prix=45)
    ecran = Produit.objects.create(nom="Écran 24 pouces", categorie=cat_elec, prix=190)
    agrafeuse = Produit.objects.create(nom="Agrafeuse", categorie=cat_bureau, prix=15)
    bloc_notes = Produit.objects.create(nom="Bloc-notes", categorie=cat_bureau, prix=5)

    # Création de magasins
    magasin_montreal = 1
    magasin_quebec = 2

    # Création de stock pour chaque produit dans chaque magasin
    for magasin in [magasin_montreal, magasin_quebec]:
        StockProduit.objects.create(produit=clavier, magasin_id=magasin, quantite=999999999)
        StockProduit.objects.create(produit=souris, magasin_id=magasin, quantite=999999999)
        StockProduit.objects.create(produit=ecran, magasin_id=magasin, quantite=999999999)
        StockProduit.objects.create(produit=agrafeuse, magasin_id=magasin, quantite=15)
        StockProduit.objects.create(produit=bloc_notes, magasin_id=magasin, quantite=50)
    
