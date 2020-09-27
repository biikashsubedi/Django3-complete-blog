from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from posts.models import *


class PostIndex(ListView):
    template_name = 'posts/index.html'
    model = Post
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostIndex, self).get_context_data(**kwargs)
        context['slider_post'] = Post.objects.all().filter(slider_post=True)
        return context


class PostDetail(DetailView):
    template_name = 'posts/detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        return context


class CategoryDetail(ListView):
    template_name = 'categories/category_detail.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        return Post.objects.filter(category=self.category).order_by('-id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        self.category = get_object_or_404(Category, pk=self.kwargs['pk'])
        context['category'] = self.category
        return context


class TagDetails(ListView):
    template_name = 'tags/tag_detail.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return Post.objects.filter(tags=self.tag).order_by('id')

    def get_context_data(self, **kwargs):
        context = super(TagDetails, self).get_context_data(**kwargs)
        self.tag = get_object_or_404(Tag, slug=self.kwargs['slug'])
        context['tag'] = self.tag
        return context
