# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
import json
from google.appengine.ext import ndb


class Curso(ndb.Model):
    firstname = ndb.StringProperty()
    lastname = ndb.StringProperty()
    gender = ndb.StringProperty()
    country = ndb.StringProperty()
    state = ndb.StringProperty()
    city = ndb.StringProperty()
    address = ndb.StringProperty()
    zipcode = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()


#
#
def salvar(firstname, lastname, gender, country, state, city, address, zipcode, phone, email):
    curso = Curso(firstname=firstname, lastname=lastname, gender=gender, country=country, state=state, city=city,
                  address=address, zipcode=zipcode, phone=phone, email=email)
    curso.put()


#
def listar(_resp):
    query = Curso.query().order(-Curso.firstname, -Curso.lastname, -Curso.gender, -Curso.country, -Curso.state,
                                -Curso.city, -Curso.address, -Curso.zipcode,-Curso.phone, -Curso.email)

    def to_dict(c):
        dct = c.to_dict()
        dct['id'] = str(c.key.id())
        return dct

    lista_de_cursos = [to_dict(c) for c in query.fetch()]
    lista_de_cursos = json.dumps(lista_de_cursos)
    _resp.write(lista_de_cursos)