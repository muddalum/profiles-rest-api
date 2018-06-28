from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission) :
    # Allow users to edit their own profile

    def has_object_permission(self, request, view, obj) :
        # Check user is trying to edit their own profile

        if request.method in permissions.SAFE_METHODS :
            return True

        # Else user is requesting a PUT/POST/DELETE, so need to check if current user is logged in and authorized to change the data it is trying to manipulate
        # Return whether the object's ID is the same as the current user's ID
        return obj.id == request.user.id

class PostOwnStatus(permissions.BasePermission) :
    # Allow users to update their own status

    def has_object_permission(self, request, view, obj) :
        # Checks the user is trying to update their own status
        # Users can view other ppl's status, but can't update them

        if request.method in permissions.SAFE_METHODS :
            return True

        return obj.user_profile.id == request.user.id
        
