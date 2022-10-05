from rest_framework import permissions

# class ProductManagerPermission(permissions.BasePermission):

#     def has_permission(self, request, view):
#         print(request.user__groups)
#         return True
        # return bool(request.user and request.group.id == 2)

    # class IsStafforReadOnly(permissions.IsAdminUser):
    
    #     def has_permission(self, request, view):
    #         if request.method in permissions.SAFE_METHODS:
    #             return True
    #         return bool(request.user and request.user.is_staff)