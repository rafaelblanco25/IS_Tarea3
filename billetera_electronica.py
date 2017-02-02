# -*- coding: utf-8 -*-

class LinkedList:
    def __init__(self):
        self.head=None
        
    def add(self, nodo):
        if self.head!=None:
            nodo.add_next(self.head)
            self.add_head(nodo)
        else:
            self.add_head(nodo)
            
    def add_head(self, nodo):
        self.head=nodo
            
class Node:
    def __init__(self, idi, fecha, monto):
        self.idi=idi
        self.fecha=fecha
        self.monto=monto
        self.next=None
        
    def add_next(self, n):
        self.next=n

class billetera_electronica:
    def __init__(self, pin, nombre, apellido, ci):
        self.nombre=nombre
        self.apellido=apellido
        self.ci=ci
        self.pin=pin
        self.creditos=LinkedList()
        self.debitos=LinkedList()
        self.saldo=0
    def saldo(self):
        return self.saldo
    
    def recargar(self, monto, fecha, idi):
        if monto<=0:
            print ("La recarga debe ser un monto mayor a 0")
            return False
        self.creditos.add(Node(idi,fecha,monto))
        self.saldo=self.saldo+monto
        return True 
        
    def consumir(self, monto, fecha, idi,pin):
        if self.pin!= pin:
            print("El pin de usuario introducido es invalido")
            return False
        
        if self.pin==pin and self.saldo>=monto:
            self.debitos.add(Node(idi,fecha,monto))
            self.saldo=self.saldo-monto
            return True
        else:
            print("El saldo no es suficiente para realizar este consumo")
            return False  
   
        