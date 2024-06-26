from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return bool(hasattr(obj, "user") and obj.user == request.user)


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.method in permissions.SAFE_METHODS)

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or hasattr(obj, "user")
            and obj.user == request.user
        )


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_staff)


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in permissions.SAFE_METHODS
            or request.user
            and request.user.is_staff
        )


class AllowPOST(permissions.BasePermission):
    def has_permission(self, request, view):
        # Permissão básica para acesso POST
        return bool(
            request.method in permissions.SAFE_METHODS or request.method == "POST"
        )
