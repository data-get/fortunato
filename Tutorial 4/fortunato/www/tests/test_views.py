import unittest

from unittest.mock import MagicMock

from ..person import Person
from ..views import IndexTemplateView


class TestIndexTemplateView(unittest.TestCase):
    def setUp(self):
        self.fortune = 'You like to test'
        self.person = MagicMock(spec=Person)
        self.person.get_fortune.return_value = self.fortune
        self.view = IndexTemplateView(person=self.person)
        self.request = MagicMock()
        self.request.method = 'GET'

    def test__init__(self):
        view = IndexTemplateView()
        self.assertIsInstance(view.person, Person)

    def test_get_context(self):
        context_data = self.view.get_context_data()
        self.assertEqual(context_data['fortune'], self.fortune)
