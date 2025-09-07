#imports
from rest_framework.permissions import BasePermission,SAFE_METHODS
from django.utils.translation import gettext_lazy as _

#permissions

class CretaedByUserOrReadOnly(BasePermission):    
    
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        if not request.user:
            return False
        
        
        return obj.created_by == request.user