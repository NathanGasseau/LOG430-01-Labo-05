from django.db import models

class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.nom


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    prix = models.FloatField()

    def __str__(self):
        return self.nom
    

class StockProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    magasin_id = models.IntegerField() 
    quantite = models.PositiveIntegerField()