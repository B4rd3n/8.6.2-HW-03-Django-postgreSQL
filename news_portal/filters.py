from django_filters import FilterSet, DateFilter, ModelMultipleChoiceFilter
from django.forms.widgets import DateInput
from django.utils.translation import pgettext_lazy
from django.forms import CheckboxSelectMultiple

from .models import Post, Category



class PostFilter(FilterSet):
    category = ModelMultipleChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label = pgettext_lazy("category", "Category name"),
        widget = CheckboxSelectMultiple(),
    )

    creation_time = DateFilter(
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