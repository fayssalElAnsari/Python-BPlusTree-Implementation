import sys
import os
sys.path.append(os.path.abspath('../src'))
from B_tree import *
import unittest


class test_b_tree(unittest.TestCase):
    elements = [5, 1, 3, 16, 10, 2, 7, 4, 20, 25, 19, 6, 8, 17, 18, 21, 23]

    def setUp(self):
        self.tree = B_tree(3, 2)

    # insert 5, 1, 3, 16, 10, 2, 7, 4, 20, 25, 19, 6, 8, 17, 18, 21, 23
    def test_root_splits(self):
        self.tree.insert(5)
        self.assertEqual(self.tree.root_node.keys, [5])
        self.assertEqual(self.tree.root_node.children, [])
        
        self.tree.insert(1)
        self.assertEqual(self.tree.root_node.keys, [1, 5])
        self.assertEqual(self.tree.root_node.children, [])

        self.tree.insert(3)
        self.assertEqual(self.tree.root_node.keys, [3])
        self.assertEqual(self.tree.root_node.children[0].keys, [1])
        self.assertEqual(self.tree.root_node.children[0].children, [])
        self.assertEqual(self.tree.root_node.children[1].keys, [5])
        self.assertEqual(self.tree.root_node.children[1].children, [])
        
        self.tree.insert(16)
        self.assertEqual(self.tree.root_node.keys, [3])
        self.assertEqual(self.tree.root_node.children[0].keys, [1])
        self.assertEqual(self.tree.root_node.children[0].children, [])
        self.assertEqual(self.tree.root_node.children[1].keys, [5, 16])
        self.assertEqual(self.tree.root_node.children[1].children, [])

        self.tree.insert(10)
        self.assertEqual(self.tree.root_node.keys, [3, 10])
        self.assertEqual(self.tree.root_node.children[0].keys, [1])
        self.assertEqual(self.tree.root_node.children[0].children, [])
        self.assertEqual(self.tree.root_node.children[1].keys, [5])
        self.assertEqual(self.tree.root_node.children[1].children, [])
        self.assertEqual(self.tree.root_node.children[2].keys, [16])
        self.assertEqual(self.tree.root_node.children[2].children, [])

        self.tree.insert(2)
        self.assertEqual(self.tree.root_node.keys, [3, 10])
        self.assertEqual(self.tree.root_node.children[0].keys, [1, 2])
        self.assertEqual(self.tree.root_node.children[0].children, [])
        self.assertEqual(self.tree.root_node.children[1].keys, [5])
        self.assertEqual(self.tree.root_node.children[1].children, [])
        self.assertEqual(self.tree.root_node.children[2].keys, [16])
        self.assertEqual(self.tree.root_node.children[2].children, [])

        self.tree.insert(7)
        self.assertEqual(self.tree.root_node.keys, [3, 10])
        self.assertEqual(self.tree.root_node.children[0].keys, [1, 2])
        self.assertEqual(self.tree.root_node.children[0].children, [])
        self.assertEqual(self.tree.root_node.children[1].keys, [5,7])
        self.assertEqual(self.tree.root_node.children[1].children, [])
        self.assertEqual(self.tree.root_node.children[2].keys, [16])
        self.assertEqual(self.tree.root_node.children[2].children, [])

        self.tree.insert(4)
        self.assertEqual(self.tree.root_node.keys, [5])
        self.assertEqual(self.tree.root_node.children[0].keys, [3])
        self.assertEqual(self.tree.root_node.children[0].children[0].keys, [1, 2])
        self.assertEqual(self.tree.root_node.children[0].children[1].keys, [4])
        self.assertEqual(self.tree.root_node.children[1].keys, [10])
        self.assertEqual(self.tree.root_node.children[1].children[0].keys, [7])
        self.assertEqual(self.tree.root_node.children[1].children[1].keys, [16])

        self.tree.insert(20)
        self.assertEqual(self.tree.root_node.keys, [5])
        self.assertEqual(self.tree.root_node.children[0].keys, [3])
        self.assertEqual(self.tree.root_node.children[0].children[0].keys, [1, 2])
        self.assertEqual(self.tree.root_node.children[0].children[1].keys, [4])
        self.assertEqual(self.tree.root_node.children[1].keys, [10])
        self.assertEqual(self.tree.root_node.children[1].children[0].keys, [7])
        self.assertEqual(self.tree.root_node.children[1].children[1].keys, [16, 20])

        self.tree.insert(25)
        self.assertEqual(self.tree.root_node.keys, [5])
        self.assertEqual(self.tree.root_node.children[0].keys, [3])
        self.assertEqual(self.tree.root_node.children[0].children[0].keys, [1, 2])
        self.assertEqual(self.tree.root_node.children[0].children[1].keys, [4])
        self.assertEqual(self.tree.root_node.children[1].keys, [10, 20])
        self.assertEqual(self.tree.root_node.children[1].children[0].keys, [7])
        self.assertEqual(self.tree.root_node.children[1].children[1].keys, [16])
        self.assertEqual(self.tree.root_node.children[1].children[2].keys, [25])

        self.tree.insert(19)
        self.assertEqual(self.tree.root_node.keys, [5])
        self.assertEqual(self.tree.root_node.children[0].keys, [3])
        self.assertEqual(self.tree.root_node.children[0].children[0].keys, [1, 2])
        self.assertEqual(self.tree.root_node.children[0].children[1].keys, [4])
        self.assertEqual(self.tree.root_node.children[1].keys, [10, 20])
        self.assertEqual(self.tree.root_node.children[1].children[0].keys, [7])
        self.assertEqual(self.tree.root_node.children[1].children[1].keys, [16, 19])
        self.assertEqual(self.tree.root_node.children[1].children[2].keys, [25])

        self.tree.insert(6)
        self.assertEqual(self.tree.root_node.keys, [5])
        self.assertEqual(self.tree.root_node.children[0].keys, [3])
        self.assertEqual(self.tree.root_node.children[0].children[0].keys, [1, 2])
        self.assertEqual(self.tree.root_node.children[0].children[1].keys, [4])
        self.assertEqual(self.tree.root_node.children[1].keys, [10, 20])
        self.assertEqual(self.tree.root_node.children[1].children[0].keys, [6, 7])
        self.assertEqual(self.tree.root_node.children[1].children[1].keys, [16, 19])
        self.assertEqual(self.tree.root_node.children[1].children[2].keys, [25])

        self.tree.insert(8)
        self.assertEqual(self.tree.root_node.keys, [5, 10])
        self.assertEqual(self.tree.root_node.children[0].keys, [3])
        self.assertEqual(self.tree.root_node.children[0].children[0].keys, [1, 2])
        self.assertEqual(self.tree.root_node.children[0].children[1].keys, [4])
        self.assertEqual(self.tree.root_node.children[1].keys, [7])
        self.assertEqual(self.tree.root_node.children[1].children[0].keys, [6])
        self.assertEqual(self.tree.root_node.children[1].children[1].keys, [8])
        self.assertEqual(self.tree.root_node.children[2].keys, [20])
        self.assertEqual(self.tree.root_node.children[2].children[0].keys, [16, 19])
        self.assertEqual(self.tree.root_node.children[2].children[1].keys, [25])

        self.tree.insert(17)
        self.assertEqual(self.tree.root_node.keys, [5, 10])
        self.assertEqual(self.tree.root_node.children[0].keys, [3])
        self.assertEqual(self.tree.root_node.children[0].children[0].keys, [1, 2])
        self.assertEqual(self.tree.root_node.children[0].children[1].keys, [4])
        self.assertEqual(self.tree.root_node.children[1].keys, [7])
        self.assertEqual(self.tree.root_node.children[1].children[0].keys, [6])
        self.assertEqual(self.tree.root_node.children[1].children[1].keys, [8])
        self.assertEqual(self.tree.root_node.children[2].keys, [17, 20])
        self.assertEqual(self.tree.root_node.children[2].children[0].keys, [16])
        self.assertEqual(self.tree.root_node.children[2].children[1].keys, [19])
        self.assertEqual(self.tree.root_node.children[2].children[2].keys, [25])

        self.tree.insert(18)
        self.assertEqual(self.tree.root_node.keys, [5, 10])
        self.assertEqual(self.tree.root_node.children[0].keys, [3])
        self.assertEqual(self.tree.root_node.children[0].children[0].keys, [1, 2])
        self.assertEqual(self.tree.root_node.children[0].children[1].keys, [4])
        self.assertEqual(self.tree.root_node.children[1].keys, [7])
        self.assertEqual(self.tree.root_node.children[1].children[0].keys, [6])
        self.assertEqual(self.tree.root_node.children[1].children[1].keys, [8])
        self.assertEqual(self.tree.root_node.children[2].keys, [17, 20])
        self.assertEqual(self.tree.root_node.children[2].children[0].keys, [16])
        self.assertEqual(self.tree.root_node.children[2].children[1].keys, [18, 19])
        self.assertEqual(self.tree.root_node.children[2].children[2].keys, [25])

        self.tree.insert(21)
        self.assertEqual(self.tree.root_node.keys, [5, 10])
        self.assertEqual(self.tree.root_node.children[0].keys, [3])
        self.assertEqual(self.tree.root_node.children[0].children[0].keys, [1, 2])
        self.assertEqual(self.tree.root_node.children[0].children[1].keys, [4])
        self.assertEqual(self.tree.root_node.children[1].keys, [7])
        self.assertEqual(self.tree.root_node.children[1].children[0].keys, [6])
        self.assertEqual(self.tree.root_node.children[1].children[1].keys, [8])
        self.assertEqual(self.tree.root_node.children[2].keys, [17, 20])
        self.assertEqual(self.tree.root_node.children[2].children[0].keys, [16])
        self.assertEqual(self.tree.root_node.children[2].children[1].keys, [18, 19])
        self.assertEqual(self.tree.root_node.children[2].children[2].keys, [21, 25])
        # print(self.tree)

        ### LEVEL 4 LAST STUPID TEST ###
        self.tree.insert(23)
        self.assertEqual(self.tree.root_node.keys, [10])
        self.assertEqual(self.tree.root_node.children[0].keys, [5])
        self.assertEqual(self.tree.root_node.children[0].children[0].keys, [3])
        self.assertEqual(self.tree.root_node.children[0].children[1].keys, [7])
        self.assertEqual(self.tree.root_node.children[0].children[0].children[0].keys, [1, 2])
        self.assertEqual(self.tree.root_node.children[0].children[0].children[1].keys, [4])
        self.assertEqual(self.tree.root_node.children[0].children[1].children[0].keys, [6])
        self.assertEqual(self.tree.root_node.children[0].children[1].children[1].keys, [8])
        self.assertEqual(self.tree.root_node.children[1].keys, [20])
        self.assertEqual(self.tree.root_node.children[1].children[0].keys, [17])
        self.assertEqual(self.tree.root_node.children[1].children[1].keys, [23])
        self.assertEqual(self.tree.root_node.children[1].children[0].children[0].keys, [16])
        self.assertEqual(self.tree.root_node.children[1].children[0].children[1].keys, [18, 19])
        self.assertEqual(self.tree.root_node.children[1].children[1].children[0].keys, [21])
        self.assertEqual(self.tree.root_node.children[1].children[1].children[1].keys, [25])
        # print(self.tree)

        ##### BEGIN DELETE TESTS #####
        self.tree2 = B_tree(4, 1)
        self.tree2.insert(10)
        self.tree2.insert(20)
        self.tree2.insert(30)
        self.tree2.insert(40)
        self.tree2.insert(50)
        self.tree2.insert(60)
        self.tree2.insert(70)
        # print(self.tree2)


        # self.tree2.delete(25)
        # print(self.tree)
        # self.tree2.delete(21)
        # print(self.tree)
        
        
    def test_battery_des_test(self):
        # TEST 1
        self.tree_test1 = B_tree(3, 2)
        for index in range(2, 37, 2):
            self.tree_test1.insert(index)
        self.tree_test1.insert([7, 9, 11, 13])
        ## verification insertion
        self.assertFalse(self.tree_test1.search_element(42)) 
        self.tree_test1.insert(42)
        self.assertTrue(self.tree_test1.search_element(42))
        # TEST 2
        self.tree_test2 = B_tree(11, 6)
        for index in range(10, 5001, 10):
            self.tree_test2.insert(index)
        for index in range(5, 4996, 10):
            self.tree_test2.insert(index)
        for N in [2, 10, 100, 1000, 10000]:
            self.tree_N = B_tree(11, 6)
            for index in range(5, 4996, N):
                self.tree_N.insert(index)
        
            


    def test_all_keys_increasing_order(self):
        self.tree.insert(self.elements)
        self.node_keys_increasing_order(self.tree.root_node)
        

    def node_keys_increasing_order(self, node):
        if node.children != None:
            for child in node.children:
                self.node_keys_increasing_order(child)
        # testing keys from down to up
        for index in range(len(node.keys)-1):
            self.assertTrue(node.keys[index] < node.keys[index+1])


    def test_all_leafs_have_no_children(self):
        # self.tree.insert(self.elements)
        # all_leafs = []
        # for child in self.tree.root_node.children:
        #     break
        pass

    
    


    def test_all_internal_nodes_have_at_most_n_minus_one_keys(self):
        pass


    def test_all_internal_nodes_have_at_most_n_children(self):
        pass


    def test_all_internal_nodes_have_at_least_n_over_two_children(self):
        pass


    def all_leaves_have_same_depth(self):
        pass


    def root_node_have_minimum_of_one_key(self):
        pass


    def all_non_leaf_nodes_have_at_least_two_children(self):
        pass


    def non_leaf_node_with_k_minus_one_keys_contains_k_children(self):
        pass


if __name__ == '__main__':
    unittest.main()