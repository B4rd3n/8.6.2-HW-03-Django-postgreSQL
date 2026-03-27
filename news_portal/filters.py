from django_filters import FilterSet, ModelChoiceFilter
from .models import Post, Category



class PostFilter(FilterSet):
    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label = 'category'
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'creation_time': ['day'],
        }