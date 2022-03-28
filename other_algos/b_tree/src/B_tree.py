from B_node import B_node

class B_tree:
    def __init__(self, parent, m):
        self.root_node = B_node(self)
        self.m = m
        self.l = [m/2]
        

    def search_element(self, element):
        self.root_node.search_element(element)
        

    def search_node(self, element):
        self.root_node.search_node(element) 

    
    def insert(self, element):
        self.root_node.insert(element)


    def main():
        print("B_tree")
        

    if __name__ == '__main__':
        main()