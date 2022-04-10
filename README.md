# Fayssal EL ANSARI
> If you are already familiar with the B-tree data structure you can skip to chapter 4.

# ABSTRACT
The idea behind this project is to give an overview of the B-tree data structure and implement the basic B-tree algorithms such as `searching`, `insertion`, and `deletion`.
B-tree is a type of data structure that insures having a balanced tree at all times (except in some cases after deletions). It is commonly used in the case of distributed data systems. 


# 1. INTRODUCTION
## HISTORY
B-trees were invented in Boeing research labs by `Edward M. McCreight` and `Rudolf Bayer`. In their paper, they consider the problem of organizing and maintaining an index for a dynamically changing random access file. An index means a collection of index elements that are pairs `(x,e)` of fixed size physically adjacent data items, namely a key `x` and some `associated information`[^1].

## USES
B-trees are generally used in `Databases` and `File Systems`. Usually, in databases, we have information stored in a distributed manner and the bottleneck isn't when communicating inside a node but rather when passing information between different nodes. Therefore it is better to have pieces of information that are related to each other in the same node or in a cluster of nodes close to each other. The same principle applies to distributed file systems. A B-tree generalizes a binary tree to have more than two values inside a node. This allows for having the positive aspects while also removing the negative aspects of having a binary tree.

![A B-Tree picture][b-tree_pic][^2]



# 2. GOALS
In this project we intend to write an optimized b-tree implementation using `python`, we have followed famous programming conventions to write easy-to-understand and maintainable code. While learning new technologies and algorithms. 

We have used previously seen notions in `object-oriented programming` courses and a python introductory course by Pierre Tirilly. We have started by working on a somewhat simpler twist on the B-tree the B-Plus tree which allows for faster traversing between neighboring nodes. This decision helped us, later on, to avoid making the same mistakes in writing the final B-tree program. 

We have also used basic `CI/CD` principles in Gitlab to automate the testing/compilation of our project.

We didn't use JIRA or similar software, instead we have simply put a `todo list` at the top of the main file in the form of a comment. Since the number of contributors isn't very big there was no need to keep track of who is responsible for a certain feature but what still needs to be done only.

# 3. TECHNICAL ASPECTS
## SET-UP

<Details>
    <Summary>How the requirements.txt file is generated</Summary>

* A virtual environment in the name of `virual_env` has been created to filter out the necessary packages for this project only.
    ```bash
    pip install virtualenv
    python -m virtualenv virtual_env
    ```
* To Activate the virtual environment:
    ```bash
    .\virtual_env\Scripts\activate  
    ```
* After installing all the necessary packages. To save them in a file:
    ```bash
    pip freeze > requirements.txt
    ```

</Details>  

* __To install the packages execute the following command__:
    ```bash
    pip install -r requirements.txt
    ```

## EXECUTE
* To test out the program you can run:
    ```bash
    cd .\other_algos\b_tree\test\
    python .\test_b_tree.py
    ```

## PROJECT STRUCTURE
```bash
├───enonces
├───other_algos
│   ├───binary_tree
│   │   ├───src
│   │   └───test
│   └───b_tree
│       ├───src
│       └───test
├───src
├───doc
└───test
```  
* `src`: Each type of tree implementation contains this folder, it has all the source code for every class of the according tree.
* `test`: Each test folder contains the tests for its neighboring `src` folder.
* `enonces`: Resides in the root; Contains the questions/hints given by the teacher for this project. 

## DESIGN CHOICES
* Naturally, we have a class for the tree which references the root node. This allows us to keep using the same reference when operating on the tree rather than updating to a new reference. Because in some cases, depending on the choice of algorithm, the root node could change.

* We have another class for the node which inherits some information from the tree class. A node can be a `root node`, an `internal node`, or a `leaf`. 
  
* Having a function calculating a state instead of updating the state manually inside a variable helps avoid possible bugs later on. Forgetting to update the state of a node for example.
  * To check whether a `node` is a `leaf` or not we simply check if its number of children is `0`. 
  * To check if a `node` is a `root node` we check for its parent, if its parent is `None` it is a root.
  * The Last case if it's not a root node nor a leaf it must be an `internal node`, there is no need to add a function for this case for the moment.

* Since the minimum number and the maximum number of keys a tree can have in its nodes can be determined manually we have these two options as params in the constructor of both the tree and the node. 

* Since the minimum is usually equal to the `max/2` this default value is applied in case the minimum was not passed in as an argument.

* The `__str__` and `__repr__` magic functions have been modified to simplify the visualization of trees/nodes.

* The conditions of having a correct tree are all stated in the test files.

## DOCUMENTATION
* To generate the documentation of a tree, cd into its root folder and run:
  ```bash

  ```

# 4. POSSIBLE MODIFICATIONS
If you intend to read and maybe also modify this program the previous chapter contains some instructions on where everything is located and the reasoning behind some design choices.

It is still possible to add these modifications to the project:
* [ ] Optimize the search algorithm to have a mix of binary search and linear search. Starting with a binary search and changing the algorithm with each step after a certain number of steps to finally come to the linear search.
  
* [ ] When inserting and deleting we can traverse the tree only one time by keeping track of all the traversed full nodes and whether or not they will be split after the queued operation. This allows for a faster operation while also avoiding failing operations in the case of multiple threads. For example, looking for a key while another is being inserted at the same time if a node is split a certain time this could lead to reporting the key as non-existent even though it is present in the tree.

* [ ] Using many threads to further optimize each operation.

* [ ] In some cases allowing duplicate keys is useful, but in some others it could lead to ambiguity.

* [ ] Other algorithms are still not finished such as the B-Plus tree.

* [ ] Adding a better way to visualize the trees.

* [ ] More generalized tests to have better flexibility when modifying later on.

<details>
  <summary>Each week's progress</summary>

#### 11/01/2022
* Introduction au projet
* Comprehension des Arbres-B 
* Premier diagramme UML des classes necessaires pour la realisation du projet
* ...


#### 18/01/2022
* Recherche BPlusTree et BTree
* pseudo code algorithm insertion
* pseudo code algorithm recherche
* PseudoCode algorithm suppression
* ...


#### 25/01/2022
* Creation de la class `BPNode.py`
* Creation du premier test d'insertion `test1()`
* Correction des algorithm d'insertion
* Passage a un `ArbreB+` au lieu d'un `BArbre`
* ...


#### 01/02/2022
* fixed splitting elements
* refactor constructor
* fixed update_keys()
* ...


#### 22/02/2022
* fixed and optimized delete function (updating keys for parent nodes)
* fixed and optimized find function
* manual testing for delete and search
* ...
</details>


[^1]: Bayer, R.; McCreight, E. (July 1970). "Organization and maintenance of large ordered indices"

[^2]: https://www.programiz.com/dsa/b-tree


[b-tree_pic]:(pics/b-tree_pic.jpg)