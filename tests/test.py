from flask import Flask
from nose.tools import assert_equal
import unittest
import os
import inicio
import tempfile
from flask.ext.testing import TestCase
from mongoengine import connect
from pymongo import MongoClient
class inicioTestCase(unittest.TestCase):
    
    def setUp(self):
        self.db_fd, inicio.app.config['DATABASE'] = tempfile.mkstemp()
        inicio.app.config['TESTING'] = True
        self.app = inicio.app.test_client()
        #inicio.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(inicio.app.config['DATABASE'])
        
    #Aqui acaba el esqueleto principal

    #Ver si la página carga Landscapes correctamente
    def test_empty(self):
        rv = self.app.get('/')
        self.assertTrue('Landscapes' in str(rv.data))

    #Ver si la página carga correctamente
    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

class Test:
    def suma(self, n1,n2):
        return n1+n2

    def testSuma(self):
        suma = Test()
        response = suma.suma(4,2)
        assert_equal(response, 6)
"""

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/')
        # assert the status code of the response
        self.assertEqual(result.status_code, 200)
"""
class BD_Test(unittest.TestCase):
    def setUp(self):
        inicio.app.config['TESTING'] = True
        inicio.app.config["MONGODB_DB"] = 'test'
        connect(
            'test',
            username='mongouser',
            password='09021993',
            host='40.117.96.16',
            port=27017
        )
        self.app = inicio.app.test_client()

    def tearDown(self):
        pass
    
    def test_create_user(self):
           client = MongoClient('mongodb://mongouser:09021993@40.117.96.16:27017')  
           db=client['test']
           db.test_collection.save(
           {
               "username": "ejemplo",
               "email": "ejemplo.mail.com"  
           })
           
if __name__ == '__main__':
    unittest.main()
