import unittest
from billetera_electronica import *

class billetera_electronicaTester(unittest.TestCase):
    def testSaldoinicial(self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563, 1204)
        #print(b.saldo())
        self.assertEqual(0,b.saldo)
        
if __name__=="__main__":
    unittest.main ()