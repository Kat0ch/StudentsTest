from rest_framework.pagination import LimitOffsetPagination


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit: int = 10
    limit_query_param: str = 'page_size'
    max_limit: int = 100
