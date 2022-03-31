import sys
import os
sys.path.append(os.path.abspath('../src'))
from B_tree import *
import unittest


class test_b_tree(unittest.TestCase):
    def setUp(self):
        self.tree = B_tree(3)

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

        ##### BEGIN DELETE TESTS #####
        self.tree.delete(25)
        print(self.tree)
        

    def test_all_keys_increasing_order(self):
        pass


    def test_all_leafs_have_no_children(self):
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