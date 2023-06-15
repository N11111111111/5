from django.views.generic import ListView,  DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Author, Category
from datetime import datetime
from django.core.paginator import Paginator
from .filters import PostFilter
from .forms import PostForm
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from .models import Post, Author, Category, User
from datetime import datetime
from .filters import PostFilter
from .forms import PostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView
from .models import *
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.http import HttpResponseRedirect



#главная страница
class PostList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'posts'
    gueryset = Post.objects.order_by('-id')



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value'] = None
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        context['form'] = PostForm()
        context['categories'] = Category.objects.all()

        return context



#найти новость или статью, фильтрация, пагинация

class SearchPosts(ListView):
    paginate_by = 3
    model = Post
    ordering = '-dateCreation'
    template_name = 'post_search.html'
    context_object_name = 'posts'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filter = PostFilter(self.request.GET, queryset)
        return self.filter.qs

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filter
        return context


#подробности о статье или новости:
class PostDetail(DetailView):
    model = Post
    template_name = 'id.news.html'
    context_object_name = 'post'


# создаем:

class PostCreateView(PermissionRequiredMixin, CreateView):
    model = Post
    template_name = 'post_create.html'
    form_class = PostForm
    context_object_name = 'post_create'
    success_url = '/news/'
    login_url=reverse_lazy('login')
    permission_required = ('news.add_post')
    # raise_exception = True

#сохраняем автора

    # def save_formset(self, request, form, formset, change):
    #     instances = formset.save(commit=False)
    #     for instance in instances:
    #         if isinstance(instance, request):
    #             if (not instance.usercreated):
    #                 instance.usercreated = Author.objects.get(authorUser=self.request.user)
    #             instance.save()


    #
    # #
    # def form_valid(self, form):
    #     # создаем форму, но не отправляем его в БД, пока просто держим в памяти
    #     fields = form.save(commit=False)
    #     if self.request.user in User.objects.all():
    #         fields.author = Author.objects.get(authorUser=self.request.user)
    #         fields.save()
    #         return super().form_valid(form)
    #     else: pass
    #
    # #
    # def post(self, request, *args, **kwargs):
    #     form = PostForm(request.POST)
    #     if self.request.user not in Author.objects.all():
    #         if form.is_valid():
    #             instance = form.save(commit=False)
    #             instance.author = Author.objects.create(authorUser=self.request.user)
    #             instance.save()
    #         return HttpResponseRedirect('/news/')
    #     return render(request, 'post_create.html', {'form': form})

# редактируем
class PostUpdateView(PermissionRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    form_class = PostForm
    context_object_name = 'post_edit'
    success_url = '/news/'
    login_url = reverse_lazy('login')
    permission_required = ('news.change_post')

#редактировать может только автор статьи
# def get_form_kwargs(self):
#     kwargs = super().get_form_kwargs()
#     if self.request.user != kwargs ['instance'].author:
#         return self.handle_no_permission()
#
#     return kwargs



# удаляем
class PostDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all
    success_url = '/news/'

    login_url = reverse_lazy('login')
    permission_required = ('news.delete_post')


    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)




