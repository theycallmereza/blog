from django.test import TestCase
from ..models import Category


class CategoriesTests(TestCase):

    def test_category_model(self):
        """Test that category model return str"""
        category = Category.objects.create(name='Django')

        self.assertEqual(category.name, str(category))
