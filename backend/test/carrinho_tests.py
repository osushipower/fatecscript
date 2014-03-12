# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import unittest
from google.appengine.ext import testbed
from mock import Mock
from web import carrinho
from web.carrinho import Produto


class CarrinhoTests(unittest.TestCase):
    def setUp(self):
        # First, create an instance of the Testbed class.
        self.testbed = testbed.Testbed()
        # Then activate the testbed, which prepares the service stubs for use.
        self.testbed.activate()
        # Next, declare which service stubs you want to use.
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()


    def listar_produtos_test(self):
        json_mock = Mock()
        carrinho.listar_produtos(json_mock)
        json_mock.assert_called_once_with([], '')
        json_mock = Mock()
        Produto(nome='Arroz', preco=5.67).put()
        carrinho.listar_produtos(json_mock)
        json_mock.assert_called_once_with([{'nome': 'Arroz', 'preco': 5.67}], '')
