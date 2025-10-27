from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Produits, Category, Tendances, Contact
from .serializers import (
    ProduitsSerializer,
    CategorySerializer,
    TendancesSerializer,
    ContactSerializer
)
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly  # ✅ Import correct depuis ton fichier permissions.py
#from .pagination import CustomPagination  #  Pagination personnalisée si tu l’as créée
from .throttling import CustomUserRateThrottle, CustomAnonRateThrottle  # ✅ Optionnel

# 🛍️ PRODUITS
class ProduitsViewSet(viewsets.ModelViewSet):
    serializer_class = ProduitsSerializer
    queryset = Produits.objects.all()

    # ✅ Ajout de la pagination, du throttling et des permissions
   # pagination_class = CustomPagination
    permission_classes = [IsAdminOrReadOnly]
    throttle_classes = [CustomUserRateThrottle, CustomAnonRateThrottle]

    # ✅ Ajout du filtrage et de la recherche
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    #filterset_fields = ['categorie__nom']
    search_fields = ['nom', 'description']
    ordering_fields = ['prix', 'nom']

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
    permission_classes = [IsAdminOrReadOnly]
    #pagination_class = CustomPagination



class TendancesViewSet(viewsets.ModelViewSet):
    queryset = Tendances.objects.all()
    serializer_class = TendancesSerializer
    permission_classes = [permissions.AllowAny]  # public
   # pagination_class = CustomPagination



class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
