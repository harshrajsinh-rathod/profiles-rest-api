from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):

    def has_obj_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):

    def has_obj_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        
        return obj.user_profile.id == request.user.id