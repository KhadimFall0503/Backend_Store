from django.db import models

# Create your models here.

class Category(models.Model):
    nom_categorie = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nom_categorie

class Produits(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    image = models.ImageField(upload_to='uploads/images/', blank=True, null=True)
    categorie = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='produits',blank=True, null=True)

    def __str__(self):
        return self.nom
    
class Tendances(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='uploads/images/', blank=True, null=True)
    produits = models.ForeignKey(Produits, on_delete=models.CASCADE, related_name='tendances')

    def __str__(self):
        return self.nom
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
    

    

    

