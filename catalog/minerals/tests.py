from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Mineral


class MineralViewsTests(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name="Abelsonite",
            category="Organic",
            color="red")

    def test_index_view(self):
        resp = self.client.get(reverse('minerals:index'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
        self.assertContains(resp, self.mineral.name)

    def test_index_sort_by_alphabet(self):
        """Test first letter sorting"""
        resp = self.client.get(reverse('minerals:index',
                                       kwargs={'letter': 'A'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn('A', resp.context['chosen'])

    def test_index_sort_by_category(self):
        """Test category sorting"""
        resp = self.client.get(reverse('minerals:index',
                                       kwargs={'category': 'Organic'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertNotIn('Borates', resp.context['chosen'])

    def test_index_sort_by_color(self):
        """Test color sorting"""
        resp = self.client.get(reverse('minerals:index',
                                       kwargs={'color': 'red'}))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertIn('red', resp.context['chosen'])

    def test_detail_view(self):
        resp = self.client.get(reverse('minerals:detail',
                                       kwargs={'pk': self.mineral.pk}))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/detail.html')
        self.assertContains(resp, self.mineral.category)
        self.assertContains(resp, "Organic")

    def test_search_view(self):
        """Test searching by parameters"""
        resp = self.client.get(reverse('minerals:search'), {'term': 'oxide'})
        resp2 = self.client.get(reverse('minerals:search'), {'term': 'red'})
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn(self.mineral, resp.context['minerals'])
        self.assertIn(self.mineral, resp2.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/index.html')
