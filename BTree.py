
'''
cette classe contiendra la definition d'un noeud 
un noeud peut etre une feuille, on definit si c'est une 
feuille par une variable isLeaf
the children is a list of nodes that are beneath this tree
...
repr
iter
next
'''
class BTree:
    
    class Node:
        def __init__(self, l, u, e):
            self.children = []
            self.elements = [e]
            self.isLeaf = True


    def __init__(self, l, u):
        self.elements = []
        self.children = []
        self.L = l
        self.U = u
        self.isLeaf = False


    get getSize(self):
        return self.


    def insert(self, e):
        self.elements.append(e)


    def delete(self, e):
        self.elements.remove(e)


