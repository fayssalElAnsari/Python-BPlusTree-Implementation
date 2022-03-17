import networkx as nx
import matplotlib.pyplot as plt
import doctest

class BPTree:
    def __init__(self, m, l):
        self.root = BPNode()
        self.m = m 
        self.l = l

    def find(self, e):
        '''
        pass in a number and see if it's already in the tree
        there must be an efficient way to look for an element without going through all the children nodes
        '''
        return self.root.find(e)

if __name__ == "__main__":
    print("no main")