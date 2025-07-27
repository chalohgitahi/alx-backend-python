from rest_framework import permissions

class IsSenderOrReceiver(permissions.BasePermission):
    """
    Custom permission to only allow the sender or receiver of a message to see it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # This check ensures that the user making the request is either the
        # sender or the receiver of the message object.
        return obj.sender == request.user or obj.receiver == request.user