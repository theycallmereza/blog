from django.test import TestCase
from ..models import Post


class PostTests(TestCase):

    def test_post_model(self):
        """Test that model return str title"""
        post = Post.objects.create(title='Django', content='some text')

        self.assertEqual(post.title, str(post))
