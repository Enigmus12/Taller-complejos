import unittest
import Taller_complejos as cplxlib

class TestCplxMethods(unittest.TestCase):

    def test_suma(self):
        c1 = (5.7, -8.9)
        c2 = (-3.4, 6.2)
        self.assertAlmostEqual(cplxlib.suma(c1, c2)[0], 2.3)
        self.assertAlmostEqual(cplxlib.suma(c1, c2)[1], -2.7)

    def test_multiplicacion(self):
        c1 = (12.3, -8.9)
        c2 = (-40.1, 1)
        self.assertAlmostEqual(cplxlib.multiplicacion(c1, c2)[0], -484.33)
        self.assertAlmostEqual(cplxlib.multiplicacion(c1, c2)[1], 369.19)

    def test_resta(self):
        c1 = (-15.3, -3.6)
        c2 = (8.4, -5.6)
        self.assertAlmostEqual(cplxlib.resta(c1, c2)[0], -23.7)
        self.assertAlmostEqual(cplxlib.resta(c1, c2)[1], 2)

    def test_division(self):
        c1 = (6.3, -2.6)
        c2 = (-3.4, 4.8)
        self.assertAlmostEqual(cplxlib.division(c1, c2)[0], -0.97976878)
        self.assertAlmostEqual(cplxlib.division(c1, c2)[1], -0.61849710)  
     
    def test_modulo(self):
        c1 = (-6.3, -2.6)
        c2 = (-3.4, 4.8)
        self.assertAlmostEqual(cplxlib.modulo(c1, c2)[0], 6.81542368)
        self.assertAlmostEqual(cplxlib.modulo(c1, c2)[1], 5.88217646)       
        
    def test_fase(self):
        c1 = (5.7, -8.9)
        c2 = (-3.4, 6.2)
        self.assertAlmostEqual(cplxlib.fase(c1, c2)[0], -1.00116435)
        self.assertAlmostEqual(cplxlib.fase(c1, c2)[1], -1.06919227)

    
    


if __name__ == '__main__':
    unittest.main()