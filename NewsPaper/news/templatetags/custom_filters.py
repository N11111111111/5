from django import template
from ..models import Author, Category, Post, PostCategory, Comment
register = template.Library()



@register.filter(name='multiply') # регистрируем наш фильтр под именем multiply, чтоб django понимал, что это именно фильтр, а не простая функция
def multiply(value, arg): # первый аргумент здесь — это то значение, к которому надо применить фильтр, второй аргумент — это аргумент фильтра, т.е. примерно следующее будет в шаблоне value|multiply:arg
    return str(value) * arg # возвращаемое функцией значение — это то значение, которое подставится к нам в шаблон

@register.filter(name='get_queryset_1')
def get_queryset_1(self):
    return Post.objects.filter(categoryType='NW')



@register.filter(name='get_queryset')
def get_queryset(self):
    return Post.objects.filter(categoryType='AR')



@register.filter(name='Censor')
def censor(value):
    MAT_LIST = [
        'мат',
        'матмат',
        'матматмат',
    ]
    for word in MAT_LIST:
        value = str(value).lower()
        value = value.replace(word, '*' * len(word))
    return value




