from nose.tools import assert_equal

# Create your tests here.
class Test:
    def suma(self, n1,n2):
        return n1+n2

    def testSuma(self):
        suma = Test()
        response = suma.suma(4,2)
        assert_equal(response, 6)
