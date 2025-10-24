from django.contrib import admin
from .models import Produits,Category,Tendances,Contact

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nom_categorie',)
    search_fields = ('nom_categorie',)
    
class TendancesAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix')
    search_fields = ('nom',)

class ProduitsAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prix', 'stock')
    search_fields = ('nom',)
    
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('name', 'email', 'message')


    
admin.site.register(Produits,ProduitsAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Tendances,TendancesAdmin)
admin.site.register(Contact,ContactAdmin)

