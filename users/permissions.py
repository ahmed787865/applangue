from rest_framework.permissions import BasePermission


class IsStaffForPost(BasePermission):
    """
    Allows access only to staff users for POST requests.
    """

    def has_permission(self, request, view):
        return (
                request.user and
                request.user.is_staff and
                request.method == 'POST'  # Allow access only for POST requests
        )
