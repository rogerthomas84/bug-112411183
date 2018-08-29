#!/usr/bin/env python

from webapp2 import WSGIApplication, Route, RequestHandler
from google.appengine.ext import ndb
from time import sleep


class TestModel(ndb.Model):

    iteration = ndb.IntegerProperty(name='i')


class MainHandler(RequestHandler):

    def home(self):
        self.response.write('<h4>Home</h4>')
        self._options()

    def show(self):
        models = TestModel.query().order(
            TestModel.iteration
        ).fetch()
        self.response.write('<h4>Show</h4>')
        for model in models:
            self.response.write('Iteration: {} - ID: {}<br />'.format(model.iteration, model.key.id()))
        self._options()

    def insert(self):
        i = 0
        while i < 10:
            m = TestModel()
            m.iteration = i
            m.put()
            i += 1

        self.response.write('<h4>Insert data</h4>')
        self.response.write('<p>Data inserted</p>')
        self._options()

    def delete(self):
        keys = TestModel.query().fetch(keys_only=True)
        ndb.delete_multi(keys=keys)

        self.response.write('<h4>Delete data</h4>')
        self.response.write('<p>Data deleted</p>')
        self._options()

    def _options(self):
        self.response.write('<a href="/insert">Insert data</a> - <a href="/show">Show data</a> - <a href="/delete">Delete data</a>')


app = WSGIApplication([
    Route('/', handler=MainHandler, methods=['GET'], handler_method='home'),
    Route('/insert', handler=MainHandler, methods=['GET'], handler_method='insert'),
    Route('/delete', handler=MainHandler, methods=['GET'], handler_method='delete'),
    Route('/show', handler=MainHandler, methods=['GET'], handler_method='show'),
], debug=True)
