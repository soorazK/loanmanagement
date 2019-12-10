from rest_framework.pagination import (
LimitOffsetPagination,
PageNumberPagination
)
class LoanLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
