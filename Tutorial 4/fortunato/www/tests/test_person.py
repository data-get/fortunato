import random
import unittest

from unittest.mock import MagicMock

from ..person import Person


class PersonTest(unittest.TestCase):
    def setUp(self):
        self.random_lib = MagicMock(spec=random)
        self.name = ''
        self.age = ''
        self.person = Person(self.name, self.age, random_lib=self.random_lib)

    def test_init(self):
        person = Person(self.name, self.age)
        self.assertEqual(person.name, self.name)
        self.assertEqual(person.age, self.age)
        self.assertEqual(person.random_lib, random)

    def test_get_fortune(self):
        expected_value = 'Test'
        self.random_lib.choice.return_value = expected_value
        fortune = self.person.get_fortune()
        self.random_lib.choice.assert_called_once_with(Person.FORTUNES)
        self.assertEqual(fortune, expected_value)
