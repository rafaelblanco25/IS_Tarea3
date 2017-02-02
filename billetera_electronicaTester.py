import unittest
import time
import sys
from billetera_electronica import *

class billetera_electronicaTester(unittest.TestCase):
    def testCaso_Frontera (self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        b.recargar(1000,time.strftime("%d/%m/%y"),2)
        b.recargar(1000,time.strftime("%d/%m/%y"),2)
        b.recargar(1000,time.strftime("%d/%m/%y"),2)
        self.assertEqual(False,b.consumir(3001,time.strftime("%d/%m/%y"),"La balconata",2))
    def testCaso_Esquina (self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        b.recargar(sys.maxint,time.strftime("%d/%m/%y"),2)
        self.assertEqual(sys.maxint,b.saldo)
    def testCaso_Esquina1 (self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        b.consumir(0,time.strftime("%d/%m/%y"),"La balconata",2)
        self.assertEqual(0,b.saldo)
    def testCaso_Malicia (self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        self.assertEqual(False,b.recargar(-2000,time.strftime("%d/%m/%y"),2))  
    def testCaso_Malicia2 (self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        self.assertEqual(False,b.consumir(-2000,time.strftime("%d/%m/%y"),"La balconata",2))  
        print ("EPA")
    def testCaso_Interior (self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        b.recargar(5000,time.strftime("%d/%m/%y"),2)
        b.consumir(3000,time.strftime("%d/%m/%y"),"La balconata",2)
        self.assertEqual(2000,b.saldo)   
    def testSaldoinicial(self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        self.assertEqual(0,b.saldo)
    def testRecarga (self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        b.recargar(5000,time.strftime("%d/%m/%y"),2)
        self.assertEqual(5000,b.saldo)     
    def testSaldoinsuficiente (self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        b.recargar(5000,time.strftime("%d/%m/%y"),2)
        self.assertEqual(False,b.consumir(6000,time.strftime("%d/%m/%y"),"La balconata",2))
    def testPininvalido (self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        b.recargar(5000,time.strftime("%d/%m/%y"),2)
        self.assertEqual(False,b.consumir(3000,time.strftime("%d/%m/%y"),"La balconata",5))    
    def testListarecargasfuncional (self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        b.recargar(5000,time.strftime("%d/%m/%y"),2)
        b.recargar(7000,time.strftime("%d/%m/%y"),2)
        self.assertEqual(7000,b.creditos.head.monto)             
    def testListadebitosfuncional (self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        b.recargar(5000,time.strftime("%d/%m/%y"),2)
        b.recargar(7000,time.strftime("%d/%m/%y"),2)
        b.consumir(3000,time.strftime("%d/%m/%y"),"La balconata",2)
        b.consumir(4000,time.strftime("%d/%m/%y"),"La balconata",2)
        self.assertEqual(4000,b.debitos.head.monto)
    def testSumadecimal (self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        b.recargar(50.5,time.strftime("%d/%m/%y"),2)
        b.recargar(100.3,time.strftime("%d/%m/%y"),2)
        self.assertEqual(150.8,b.saldo)
    def testSumadeRecargas(self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        b.recargar(2000,time.strftime("%d/%m/%y"),2)
        b.recargar(5000,time.strftime("%d/%m/%y"),2)
        b.recargar(8000,time.strftime("%d/%m/%y"),2)
        self.assertEqual(15000,b.saldo)  
    def testRestadeSaldo(self):
        b=billetera_electronica(2,"Rafael", "Blanco", 24981563)
        b.recargar(2000,time.strftime("%d/%m/%y"),2)
        b.recargar(5000,time.strftime("%d/%m/%y"),2)
        b.consumir(3000,time.strftime("%d/%m/%y"),"La balconata",2)
        self.assertEqual(4000,b.saldo)  
         
    
        

        
        
if __name__=="__main__":
    unittest.main ()