from rest_framework import serializers
from .models import Produits,Category,Tendances

class ProduitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produits
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class TendancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tendances
        fields = '__all__'
