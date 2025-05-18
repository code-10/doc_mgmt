from rest_framework.permissions import BasePermission, SAFE_METHODS

'''
    This is an assumption just to showcase role based operations, we can do whatever custom logic we want in permissions
'''
class IsAdminEditorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated and request.user.role in ['admin', 'editor']
