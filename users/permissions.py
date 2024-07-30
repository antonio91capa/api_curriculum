from rest_framework.permissions import BasePermission
from .models import User


class IsStandardUser(BasePermission):
    def has_permission(self, request, view):
        try:
            user = User.objects.get(email=request.user, is_recruiter=False)
        except User.DoesNotExist:
            return False
        return True
