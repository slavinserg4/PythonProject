from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 12

    def get_paginated_response(self, data):
        return Response({
            'total': self.page.paginator.count,
            'total_pages': self.page.paginator.num_pages,
            'previous': bool(self.get_previous_link()),
            'next': bool(self.get_next_link()),
            'results': data
        })

