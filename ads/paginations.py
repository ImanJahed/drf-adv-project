from rest_framework.pagination import PageNumberPagination
from django.conf import settings


class StandardSetPagination(PageNumberPagination):
    page_size = getattr(settings, 'PAGE_SIZE_PAGINATION', 1)
