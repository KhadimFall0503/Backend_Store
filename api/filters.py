import django_filters
from .models import Produits

class ProduitsFilter(django_filters.FilterSet):
    nom = django_filters.CharFilter(field_name='nom', lookup_expr='icontains')
    categorie_id = django_filters.NumberFilter(field_name='categorie_id')
    prix_min = django_filters.NumberFilter(field_name='prix', lookup_expr='gte')
    prix_max = django_filters.NumberFilter(field_name='prix', lookup_expr='lte')

    class Meta:
        model = Produits
        fields = ['nom', 'categorie_id', 'prix_min', 'prix_max']
