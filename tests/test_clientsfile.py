from unittest import TestCase
from clientsfile import Clients


class TestClients(TestCase):

    def test_imc(self):
        cliente01 = Clients("Alana Lima", 25, 40, 1.61)
        cliente01.imc()
