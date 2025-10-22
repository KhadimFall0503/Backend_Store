
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from api.views import ProduitsViewSet,CategoryViewSet,TendancesViewSet

router = DefaultRouter()
router.register(r'produits', ProduitsViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tendances', TendancesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
