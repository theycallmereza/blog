from django.views import generic

from .models import Post


# Create your views here.
class HomepageView(generic.ListView):
    queryset = Post.objects.filter(status='published')
    template_name = 'index.html'
    context_object_name = 'posts'
