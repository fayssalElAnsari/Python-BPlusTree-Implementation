from B_node import B_node

class B_tree:
    def main():
        print("B_tree")

    def __init__(self, parent):
        self.root_node = B_node(self)
        

    def search_element(self, element):
        self.root_node.search_element(element)
        

    def search_node(self, element):
        self.root_node.search_node(element) 


    if __name__ == '__main__':
        main()