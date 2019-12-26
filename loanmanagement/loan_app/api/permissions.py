from rest_framework import permissions


class NewPermission(permissions.BasePermission):
    def has_permission(self, request,view):
        # print(request.META)
        # print(dir(request))
        print(request.auth)
        print(request.user)
        return True