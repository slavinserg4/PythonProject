from django_filters import rest_framework as filters
class PizzaFilter(filters.FilterSet):
    lt = filters.NumberFilter(field_name='price', lookup_expr='lt')
    range = filters.RangeFilter(field_name='size')
    price_in = filters.BaseInFilter(field_name='price')

    order = filters.OrderingFilter(
        fields=(
            ('id', 'id'),
            ('price', 'price'),
            ('size', 'size'),
        )
    )