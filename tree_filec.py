class Node:
    def __init__(self, identifier):
        self.__identifier = identifier
        self.__children = []

    def identifier(self):
        return self.__identifier

    def children(self):
        return self.__children

    def add_child(self, identifier):
        self.__children.append(identifier)

n = Node("e")
n.identifier()
n.add_child("r")
n.children()

class Tree:
    def __init__(self):
        self.__nodes = {}

    def nodes(self):
        return self.__nodes

    def add_node(self, identifier, parent=None):
        node = Node(identifier)
        self.__nodes[identifier] = node

        if parent is not None:
            self.__nodes[parent].add_child(identifier)

        return None

    def is_empty(self):
        if self.nodes() == {}:
            return True
        else:
            return False

    def is_a_leaf(self, identifier):
        if self.__nodes[identifier].children() == []:
            return True
        else:
            return False

    def list_leaf(self):
        d = []
        for a in self.nodes():
            if self.is_a_leaf(a):
                d += [a]
        return d

    def is_root(self, identifier):
        d = True
        for a in self.__nodes.keys():
            if not identifier in self.__nodes[a].children():
                d = True and d
            else:
                d = False and d
        return d

    def ancestor(self, identifier):
        d = 0
        z = []
        if self.is_root(identifier):
            print("no ancestor for root_node")
        else:
            if identifier not in self.__nodes.keys():
                print("no such node in tree")
            else:
                for a in self.__nodes.keys():
                    if identifier in self.nodes()[a].children():
                        d += 1
                        z += [a]
                if d == 1:
                    return z[0]
                else:
                    print("the tree is not well_formed")

    def one_way_to_root(self, identifiant):
        if self.is_root(identifiant):
            return True
        else:
            return self.one_way_to_root(self.ancestor(identifiant))

    def one_and_only_root(self):
        d = 0
        for a in self.nodes().keys():
            if self.is_root(a):
                d += 1
        if d == 1:
            return True
        else:
            return False

    def well_formed(self):
        d = True
        for a in self.list_leaf():
            if self.one_and_only_root() and self.one_way_to_root(a):
                d = True and d
            else:
                d = False and d
        return d

    def belongs_to_tree(self, identifier):
        if identifier not in self.nodes().keys():
            print("no such node in tree")
            return False
        else:
            return True

    def branch_level(self, identifiant):
        if self.well_formed():
            if self.belongs_to_tree(identifiant):
                if self.is_root(identifiant):
                    return 0
                else:
                    return 1 + self.branch_level(self.ancestor(identifiant))

    def list_of_node_at_level_n(self, n):
        d = []
        for a in self.nodes():
            if self.branch_level(a) == n:
                d += [a]
        return d

    def profondeur(self):
        d = self.branch_level(self.list_leaf()[0])
        for a in self.list_leaf():
            d = min(d, self.branch_level(a))
        return d

    def hauteur(self):
        d = 0
        for a in self.list_leaf():
            d = max(d, self.branch_level(a))
        return d

t1 = Tree()
t1.add_node("e")
t1.is_empty()
t1.nodes()
t1.is_a_leaf("e")
t1.list_leaf()
t1.is_root("e")
t1.add_node("r")
t1.one_and_only_root()
t1.ancestor("r")

t2 = Tree()
t2.add_node("t")
t2.add_node("r" , "t")
t2.ancestor("r")
t2.ancestor("e")
t2.ancestor("t")
t2.profondeur()
t2.branch_level("r")
t2.list_of_node_at_level_n(1)
t2.list_of_node_at_level_n(2)
t2.hauteur()






class Assoc_Table:
    def __init__(self):
        self.__eqtable = []

    def eqtable(self):
        return self.__eqtable

    def add_class(self, eqclass):
        self.__eqtable += [eqclass]

    def add_element_to_class(self, identifiant, eqclass):
        self.__eqtable.remove(eqclass)
        eqclass += [identifiant]
        return self.add_class(eqclass)

    def well_formed_eqtable(self):
        for a in self.eqtable():
            for b in a:
                 self.eqtable().remove(a)
                 for c in self.eqtable() :
                    if b in c:
                        return False
                 self.add_class(a)
        return True

    def get_element_class(self, element):
        d = 0
        if self.well_formed_eqtable():
            for a in self.eqtable():
                if element in a:
                    d += 1
                    return a
            if not d == 1:
                return [element]


    def add_element_to_element_class(self, element1, element2):
        c = self.get_element_class(element2)
        return self.add_element_to_class(element1, c)

    def element_eq_to_element(self, element1, element2):
        if element2 in self.get_element_class(element1):
            return True
        else:
            return False

    def list_of_equivalence_class(self, list):
        t = []
        for a in list:
            t += self.get_element_class(a)
        return t


a = Assoc_Table()
a.eqtable()
a.add_class( ["a"])
a.add_element_to_class("e" , ["a"] )

print(a.eqtable())

a.well_formed_eqtable()
print(a.get_element_class("e"))
a.add_element_to_element_class("c" , "e")
print(a.element_eq_to_element("a" , "c"))
print(a.list_of_equivalence_class(["u"]))

def compare_list_to_list(l1, l2, AssocTable):
    d = []
    c = []
    for a in l1:
        if not a in AssocTable.list_of_equivalence_class(l2):
            d += [a]
    for b in l2:
        if not b in AssocTable.list_of_equivalence_class(l1):
            c += [b]
    return [d, c]

t = Assoc_Table()
t.add_class([1,4])

print(compare_list_to_list([1,2,3,5] , [1,4,5,7] , t ))


def recursive_adding_node(tree, h, a):
    c = 0
    if h == 0:
        return tree
    else:
        tree.add_node(c, a)
        return recursive_adding_node(tree, h - 1, c )

t3 = Tree()
t3.add_node("a" )
print(recursive_adding_node(t3 , 4 , "a").nodes())

def add_none_existing_node_to_tree(A1, A2):
    h = max(A1.hauteur(), A2.hauteur())
    if h == A1.hauteur():
        a = A2.list_leaf()[0]
        return A1, recursive_adding_node(A2, h, a)
    else:
        a = A1.list_leaf()[0]
        return recursive_adding_node(A1, h, a), A2


def compare_tree_to_tree(A1, A2, AssocTable):
    d = []
    h = max(A1.hauteur(), A2.hauteur())
    for i in range(h+1):
        d += [compare_list_to_list(A1.list_of_node_at_level_n(i), A2.list_of_node_at_level_n(i) , AssocTable)]
    return d

t4 = Tree()
t4.add_node("a")

t5 = Tree()
t5.add_node("e")
t5.add_node("r" , "e")

u = Assoc_Table()

print(compare_tree_to_tree(t4 , t5 , u  ))


t6 = Tree()
t6.add_node("a")
t6.add_node("r" , "a" )
t6.add_node( "t" , "a")

t7 = Tree()
t7.add_node("y")

v = Assoc_Table()
v.add_class(["a"  ,"y" ])

print(compare_tree_to_tree(t6 , t7 , v ))


def allowed_word(identifiant):
    if identifant == "block" or identifiant == "end" or identifiant == "port":
        return False
    else:
        return True

def parse_block(file , tree , current_node):
    x = get_word(file)
    if allowed_word( x ):
        if current_node == None:
            tree.add_node(x)
            current_node = x
        else:
            tree.add_node(x , current_node)
            current_node = x
        b = get_word(file)
        if allowed_word(b):
            print ( " the model is not well formed")
        else :
            if b == "block":
                parse_block(file , tree , current_node)
            elif b == "port":
                parse_port(file ,tree , current_node)
