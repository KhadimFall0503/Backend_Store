from rest_framework import viewsets
from .models import Produits, Category, Tendances, Contact
from .serializers import ProduitsSerializer, CategorySerializer, TendancesSerializer, ContactSerializer

class ProduitsViewSet(viewsets.ModelViewSet):
    serializer_class = ProduitsSerializer
    queryset = Produits.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search')
        categorie_id = self.request.query_params.get('categorie')

        if search:
            queryset = queryset.filter(nom__icontains=search)
        if categorie_id:
            queryset = queryset.filter(categorie_id=categorie_id)
        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TendancesViewSet(viewsets.ModelViewSet):
    queryset = Tendances.objects.all()
    serializer_class = TendancesSerializer
    
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
