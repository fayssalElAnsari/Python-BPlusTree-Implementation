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
│       └───test
├───src
├───doc
└───test
```  


## Algorithm de recherche
*   Complexite: `O(log(N))`
    * Explication: N: Dans le pire des cas on a: `O(log m/2 (N))` et meilleur cas arbre equilibree `O(Log m (N))`
                      `O(Log m (N) * Log (m))` multiplication par constant donc le m disparait
*   Description: 
    1. Verifier si l'element `k` existe dans la liste des cles actuels
    2. Verifier si Le noeud actuel est une feuille
    3. Appele recursive sur chaque enfant du neoud actuel


## Algorithm d'insertion
*   Complexite: `O(log(N))`
    *   Explication: Utilisation de l'algorithm de recherche avant d'inserer
*   Description:


## Algorithm de suppression
*   Complexite: `O(log(N))`
    *   Explication: Utilisation de l'algorithm de recherche avant de supprimer
*   Description: 


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

