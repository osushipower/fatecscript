# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from google.appengine.ext import ndb


class Produto(ndb.Model):
    nome = ndb.StringProperty(required=True)
    preco = ndb.FloatProperty(default=5)


def index(_resp):
    _resp.write('Olá Mundo!')


def adicionar_produto(nome, preco):
    produto = Produto(nome=nome, preco=float(preco))
    produto.put()


def listar_produtos(_json):
    query = Produto.query()
    query = query.order(Produto.nome)
    produtos = query.fetch()
    produtos_dct = [p.to_dict() for p in produtos]
    _json(produtos_dct,'')
