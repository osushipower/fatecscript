# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from google.appengine.ext import ndb


class Produto(ndb.Model):
    nome = ndb.StringProperty(required=True)
    preco = ndb.FloatProperty(default=5)

    def to_dict(self, include=None, exclude=None):
        dct = super(Produto, self).to_dict(include=None, exclude=None)
        dct['id'] = str(self.key.id())
        return dct


def index(_write_tmpl):
    _write_tmpl('templates/carrinho.html')


def adicionar_produto(_json, nome, preco):
    produto = Produto(nome=nome, preco=float(preco))
    produto.put()
    _json(produto.to_dict())


def listar_produtos(_json):
    query = Produto.query()
    query = query.order(Produto.nome)
    produtos = query.fetch()
    produtos_dct = [p.to_dict() for p in produtos]
    _json(produtos_dct, '')

def apagar_produto(id):
    key=ndb.Key(Produto,int(id))
    key.delete()