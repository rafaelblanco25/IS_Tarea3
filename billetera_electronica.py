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
    def __init__(self, id, fecha, monto):
        self.id=id
        self.fecha=fecha
        self.monto=monto
        self.next=None
        
    def add_next(self, n):
        self.next=n

class billetera_electronica:
    def __init__(self, id, nombre, apellido, ci, pin):
        self.id=id
        self.nombre=nombre
        self.apellido=apellido
        self.ci=ci
        self.pin=pin
        self.creditos=LinkedList()
        self.debitos=LinkedList()
        self.saldo=0
        
    def saldo(self):
        return self.saldo
    
    def recargar(self, monto, fecha, id):
        self.creditos.add(Node(id,fecha,monto))
        self.saldo=self.saldo+monto
        return True 
        
    def consumir(self, monto, fecha, id,pin):
        if self.pin==pin and self.saldo>=monto:
            self.consumos.add(Node(id,fecha,monto))
            self.saldo=self.saldo-monto
            return True
        else:
            print("El saldo no es suficiente para realizar este consumo")
            return False      
def main():
    l=LinkedList()
    n=Node(1,12,300)
    l.add(n)
    print(l.head.id)

if __name__=="__main__":
    main()
        
    