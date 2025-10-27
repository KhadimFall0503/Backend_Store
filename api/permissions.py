from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Lecture pour tous, modification seulement pour les administrateurs.
    """
    def has_permission(self, request, view):
        # SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Seul le propriétaire de l'objet peut le modifier ou le supprimer.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
