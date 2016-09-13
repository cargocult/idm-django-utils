from django.test import TestCase

import models

class TestPickleField(TestCase):
    def test_default(self):
        m = models.TestModel()
        self.assertEqual(m.pickle_data, None)

    def test_set(self):
        m = models.TestModel()
        data = dict(foo=1, bar=2)
        m.pickle_data = data
        m.save()
        m = models.TestModel.objects.get(pk=m.id)
        self.assertEqual(m.pickle_data, data)
