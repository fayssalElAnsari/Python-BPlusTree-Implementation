# L3_INFO_Projet_EL-ANSARI
L3-INFO-G6


## Buts
* l'utilisation des notions deja vues en POO/COO pour realiser le projet demande. 
* Introduction a des nouveaux algorithms
* Apprentissage de nouvelles technologies


## Description du projet
Dans ce projet on va essaayer d'implementer la structure des donnees des B-Arbres en utilisant python. Ces arbres devrait avoir les fonctinalites suivantes:
* `Rechercher` l'existance d'un element dans cet arbre.
* `Insertion` d'un element dans un B-Arbre.
* `Suppression` d'un element du B-arbre.


## Structure du projet
```bash
├───enonces
├───other_algos
│   ├───binary_tree
│   │   ├───src
│   │   └───test
│   └───b_tree
│       ├───src
│       │   └───__pycache__
│       └───test
├───src
└───test
    └───__pycache__
```  


## Resumee des livrables
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

