from rest_framework.pagination import LimitOffsetPagination

# FIXME: пагинатор - это не сервис.
#  CoursesStats.get - внутри этого метода - бизнес логика =>
#  можно было вынести в сервис
class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit: int = 10
    limit_query_param: str = 'page_size'
    max_limit: int = 100
