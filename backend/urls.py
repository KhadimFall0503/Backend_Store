
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from api.views import ProduitsViewSet,CategoryViewSet,TendancesViewSet,ContactViewSet

router = DefaultRouter()
router.register(r'produits', ProduitsViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tendances', TendancesViewSet)
router.register(r'contacts', ContactViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path(r'^api/auth/', include('djoser.urls')),
    re_path(r'^api/auth/', include('djoser.urls.authtoken')),
    re_path(r'^api/auth/', include('djoser.urls.jwt')),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
