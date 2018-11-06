class Node:
        def __init__(self , identifier):
            self.__identifier = identifier
            self.__children = []

        def identifier(self):
            return self.__identifier

        def children(self):
            return self.__children

        def add_child(self , identifier):
            self.__children.append(identifier)

class Tree:
    def __init__(self):
        self.__nodes = {}

    def nodes(self):
        return self.__nodes

    def add_node(self , identifier , parent = None):
        node = Node(identifier)
        self.__nodes[identifier] = node

        if parent is not None :
            self.__nodes[parent].add_child(identifier)

        return None

    def is_empty(self):
        if self.nodes() == {}:
            return True
        else :
            return False

    def is_a_leaf(self , identifier ):
        if self.__nodes[identifier].__children == [] :
            return True
        else :
            return False

    def list_leaf(self):
        d = []
        for a in self.nodes():
            if self.is_a_leaf(a):
                d += [a]
        return d

    def is_root(self , identifier):
        d = True
        for a in self.__nodes[key]:
            if not identifier in self.__nodes[a].__children:
                d = True and d
            else :
                d = False and d
        return d

    def ancestor(self,identifier):
        d = 0
        z = []
        if  is_root(self,identifier):
            print("no ancestor for root_node")
        else :
            if identifier not in self._nodes[key]:
                print("no such node in tree")
            else :
                for a in self.__nodes[key]:
                    if identifier in self.nodes[a].__children:
                        d += 1
                        z += [ a]
                if d = 1 :
                    return z[0]
                else :
                    print("the tree is not well_formed")

    def one_way_to_root(self , identifiant):
        if self.is_root(identifiant):
            return True
        else :
            return  one_way_to_root(self , self.ancestor(identifiant))

    def one_and_only_root(self ):
        d = 0
        for  a in self.nodes()[key]:
            if self.is_root(a):
                d += 1
        if d = 1 :
            return True
        else :
            return False

    def well_formed(self):
        for a in self.list_leaf():
            if self.one_and_only_root() and self.one_way_to_root(a):
                d = True and d
            else :
                d = False and d
        return d



    def belongs_to_tree(self, identifier):
        if identifier not in self.nodes()[key]:
            print("no such node in tree")
            return False
        else :
            return True

    def branch_level(self,identifiant):
        if well_formed(self):
            if  self.belongs_to_tree(identifiant):
                if self.is_root(identifiant):
                    return 0
                else :
                    return 1 + branch_level(self , self.ancestor(identifiant))


    def list_of_node_at_level_n(self, n ):
        for a in self.nodes():
            if self.branch_level(a) == n :
                d += [a]
        return d

    def profondeur(self , identifiant):
        d = branch_level(self.list_leaf()[0])
        for a in self.list_leaf():
            d = min(d , self.branch_level(identifiant))
        return d

    def hauteur(self , identifiant):
        d = 0
        for a in self.list_leaf():
            d = max(d , self.branch_level(identifiant))



class Assoc_Table :
    def __init__(self):
        self.__eqtable = []

    def eqtable(self):
        return self.__eqtable

    def add_class(self , eqclass  ):
        self.__eqtable += [eqclass]

    def add_element_to_class(self , identifiant , eqclass ):
        self.eqtable() = self.eqtable().remove(eqclass)
        eqclass += [identifiant]
        return self.add_class(eqclass)

    def well_formed_eqtable(self):
        for a in self.eqtable():
            for b in a:
                for c in self.eqtable().remove(a):
                    if b in c:
                        return False
        return True


    def get_element_class(self , element):
        if well_formed_eqtable(self):
            for a in self.eqtable():
                if element in a :
                    return a

    def add_element_to_element_class(self, elmement1 , element2 ):
        c = self.get_element_class(element2)
        return  self.add_element_to_class(element1 , c )


    def element_eq_to_element(self , element1 , element2 ):
        if  element2 in self.get_element_class(element1):
            return True
        else :
            return False

    def list_of_equivalence_class(self , list):
        d =[]
        for a in list :
            d += self.get_element_class(a)
         return d


def compare_list_to_list(l1 , l2 , AssocTable):
    d =[]
    c = []
    for a in l1:
        if not a in AssocTable.list_of_equivalence_class(l2):
            d += [a]
    for b in l2 :
        if not b in AssocTable.list_of_equivalence_class(l1):
            c += [b]
    return [b ,c]

def recursive_adding_node(    tree , h , a ):
    if h = 0 :
        return tree
    else :
        return recursive_adding_node(tree.add_node(a , "i") , h-1 , "i")

def add_none_existing_node_to_tree(A1 , A2):
    h = max( A1.hauteur() , A2.hauteur())
    if h = A1.hauteur():
        a = A2.list_leaf()[0]
        return  A1 , recursive_adding_node(A2 , h , a )
    else :
        a = A1.list_leaf()[0]
        return  recursive_adding_node(A1 , h , a ) , A2

def compare_tree_to_tree(A1 , A2 , AssocTable ):
    d = []
    A1 ,A2 = add_none_existing_node_to_tree(A1 , A2)
    h = A1.hauteur()
    for i in range(h):
        d += [compare_list_to_list(A1.list_of_node_at_level_n(i) , A2.list_of_node_at_level_n(i))]
    return d



def allowed_word(identifiant):
    if identifant == "block" or identifiant == "end" or identifiant == "port":
        return False
    else :
        return True


def parse_block(file , tree):
    if is_empty(file):
        return  memory
    else:
        a = get_word(file)
        if allowed_word(file , a ):
            




def parser(file) :
    a = get_word(file)
    if a == "block":
        parse_block(file)
    elif a == "port":
        parse_port(file)
    else a == "end":
        parse_ending(file)

#
# Main part
#
n1 = Node("n1")



