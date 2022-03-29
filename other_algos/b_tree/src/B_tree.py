from B_node import B_node

class B_tree:
    def __init__(self, m):
        self.m = m
        self.l = [m/2]
        self.root_node = B_node(self)
        self.parent = None
        self.keys = []
        self.children = []
        

    def search_element(self, element):
        self.root_node.search_element(element)
        

    def search_node(self, element):
        self.root_node.search_node(element) 

    
    def insert(self, element):
        self.root_node.insert(element)


    def main():
        print("B_tree")

    
    def digraph(self):
        header1 = "digraph {"
        header2 = "node [shape = record,height=.1];"
        arcs = ""
        nodes = ""
        body = ""
        footer = " }"    
        return header1 + header2 + body + footer


    def __repr__(self):
       return "{\"keys\": " + str(self.root_node.keys) + ", \"children\": "+str(self.root_node.children) +"}" 


    def __str__(self):
        return "{\"keys\": " + str(self.root_node.keys) + ", \"children\": "+str(self.root_node.children) +"}"
        

    if __name__ == '__main__':
        main()