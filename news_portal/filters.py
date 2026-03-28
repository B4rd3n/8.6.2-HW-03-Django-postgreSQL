from django_filters import FilterSet, ModelChoiceFilter, DateFilter, Filter
from django.forms import DateField, Field
from django.forms.widgets import DateInput, SelectDateWidget

from .models import Post, Category



class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label = 'category'
    )
    creation_time = Filter(
        field_name='creation_time',
        widget=DateInput(
            attrs={'type': 'date'}
        ),
        lookup_expr='date',
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
        }