from django.test import TestCase
from django.urls import reverse, resolve

from ..models import Post
from ..views import HomepageView, PostListView


def sample_post(title='Title One', slug='title-one'):
    """Create a sample post"""
    return Post.objects.create(title=title, slug=slug, content="Some text ...")


class PostTests(TestCase):

    def test_post_model(self):
        """Test that model return str title"""
        post = Post.objects.create(title='Django', content='some text')

        self.assertEqual(post.title, str(post))

    def test_posts_representation_in_homepage(self):
        """Test show latest posts in home page"""
        post1 = sample_post(title='Custom Django user model', slug='custom-django-user-model')
        post1.status = 'published'
        post1.save()
        post2 = sample_post(title="Draft Post", slug='draft-post')

        url = reverse('home')
        response = self.client.get(url)
        view = resolve('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, post1.title)
        self.assertNotContains(response, post2.title)
        self.assertEqual(
            view.func.__name__,
            HomepageView.as_view().__name__
        )

    def test_post_list(self):
        """Test show all posts"""
        post1 = sample_post(title='Custom Django user model', slug='custom-django-user-model')
        post1.status = 'published'
        post1.save()
        post2 = sample_post(title="Draft Post", slug='draft-post')

        url = reverse('post-list')
        response = self.client.get(url)
        view = resolve('/posts/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post-list.html')
        self.assertContains(response, post1.title)
        self.assertNotContains(response, post2.title)
        self.assertEqual(
            view.func.__name__,
            PostListView.as_view().__name__
        )
