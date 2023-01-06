from django.forms import DateTimeInput
from django_filters import FilterSet, DateTimeFilter
from .models import Post


class PostFilter(FilterSet):
    dateTimeCreation = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='lt',
        label='Дата меньше',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )


    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'category_type': ['contains'],
        }