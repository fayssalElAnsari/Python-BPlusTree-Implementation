
'''
In computer science, a B-tree is a self-balancing tree data structure
that maintains sorted data and allows searches,
sequential access, insertions, and deletions in logarithmic time:
1. Every node has at most m children.
2. Every non-leaf node (except root) has at least ⌈m/2⌉ child nodes.
3. The root has at least two children if it is not a leaf node.
4. A non-leaf node with (k) children contains (k-1) keys.
5. All leaves appear in the same level and carry no information.
...
repr
iter
next
'''
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


