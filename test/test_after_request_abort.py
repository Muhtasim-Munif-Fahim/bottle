# -*- coding: utf-8 -*-
from bottle import Bottle, abort, response
from .tools import ServerTestBase


class TestAfterRequestAbortHeaders(ServerTestBase):
    def test_after_request_headers_survive_abort(self):
        @self.app.hook('after_request')
        def add_header():
            response.headers['abc'] = 'yes'

        @self.app.get('/abort')
        def boom():
            abort(424)

        status, headers, body = self.urlopen('/abort')
        self.assertEqual(424, int(status.split()[0]))
        self.assertEqual('yes', headers.get('abc') or headers.get('Abc'))
