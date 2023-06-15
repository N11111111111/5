from django_filters import FilterSet
from .models import Post, Author


# создаём фильтр
class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {
                'author': ['exact'],
                'dateCreation': ['gt'],
                'title': ['icontains'],
                'categoryType': ['exact']
            }

