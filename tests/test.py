
from flask import Flask
from nose.tools import assert_equal
from flask.ext.testing import TestCase
# Create your tests here.
class Test:
    def suma(self, n1,n2):
        return n1+n2

    def testSuma(self):
        suma = Test()
        response = suma.suma(4,2)
        assert_equal(response, 6)

'''
class TestNotRenderTemplates(TestCase):

    render_templates = False

    def test_assert_not_process_the_template(self):
        response = self.client.get("/template/")

        assert "" == response.data
'''
