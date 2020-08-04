from django.views import generic

from .models import Post


# Create your views here.
class HomepageView(generic.ListView):
    queryset = Post.objects.filter(status='published')
    template_name = 'index.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(HomepageView, self).get_context_data(**kwargs)
        context['home'] = 'active'
        return context


class PostListView(generic.ListView):
    queryset = Post.objects.filter(status='published')
    template_name = 'blog/post-list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['blog'] = 'active'
        return context


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
    context_object_name = 'post'
