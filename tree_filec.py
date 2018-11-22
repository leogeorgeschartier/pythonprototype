class Node:
    BLOCK=1
    PORT=2
    IDENTIFIER=3
    CLASS=4


    def __init__(self, identifier ,type):
        self.__identifier = identifier
        self.__children = []
        self.__type = type


    def identifier(self):
        return self.__identifier

    #def children(self):
        #return self.__children

    #def add_child(self, identifier):
        #self.__children.append(identifier)

n = Node("e",Node.BLOCK)
n.identifier()
#n.add_child("r")
#n.children()

class Tree:
    def __init__(self):
        self.__nodes = []

    def __init__(self,listnodes):
        assert isinstance(listnodes, list)
        self.__nodes = listnodes

    def nodes(self):
        return self.__nodes


    def listnodess(self):
        def iterate( l , f ):
            if l == []:
                return l
            else :
                return f(l[0]) + iterate(l[1:] , f )
        def loxa( l ):
            if l == []:
                return l
            else :
                return [l[0]] + iterate(l[1:] , loxa)
        return loxa(self.nodes())


    def is_empty(self):
        if self.nodes() == []:
            return True
        else:
            return False

    def addroot(self , node):
        if self.is_empty():
            self.__nodes += [node , []]


    def root(self):
        if self.__nodes == []:
            print("the tree is empty")
        else :
            return self.nodes()[0]


    def belongstotree(self, x):
        def belongsto(arbre , x):
            if arbre == []:
                return False
            else:
                if arbre[0] == x:
                    return True
                else:
                    if not belongsto(arbre[1], x):
                        if len(arbre) < 3:
                            return False
                        else:
                            return belongsto([arbre[0]] + arbre[2:], x)
                    else:
                        return True
        t = self.nodes()
        return belongsto(t , x )






    def subtreey(self, a):
        def subtree(arbre , a):
            if arbre == []:
                return None
            else:
                if arbre[0] == a:
                    return arbre
                else:
                    if subtree(arbre[1], a) == None:
                        if len(arbre) < 3:
                            return None
                        else:
                            return subtree([arbre[0]] + arbre[2:], a)
                    else:
                        return subtree(arbre[1], a)
        t = Tree(subtree(self.nodes() , a))
        return t

    def childnode(self , node):
        t = self.subtreey(node)
        def get_first(l):
            d = []
            if l == []:
                return l
            else:
                d += l[0][0] + get_first(l[1:])
            return d
        if self.is_a_leaf(node):
            return []
        else :
            return get_first(t.nodes()[1:])


    def addnod(self , x , y):
        def belongsto(arbre , x):
            if arbre == []:
                return False
            else:
                if arbre[0] == x:
                    return True
                else:
                    if not belongsto(arbre[1], x):
                        if len(arbre) < 3:
                            return False
                        else:
                            return belongsto([arbre[0]] + arbre[2:], x)
                    else:
                        return True
        def addnode(tree, a, b):
            if tree == []:
                return tree
            else:
                if not belongsto(tree, b):
                    return tree
                else:
                    if tree[0] == b:
                        if [] in tree:
                            tree.remove([])
                            return tree + [[a, []]]
                        else:
                            return tree + [[a, []]]
                    else:
                        if belongsto(tree[1], b):
                            if len(tree) >= 3:
                                return [tree[0]] + [addnode(tree[1], a, b)] + tree[2:]
                            else:
                                return [tree[0]] + [addnode(tree[1], a, b)]
                        else:
                            if len(tree) < 3:
                                return tree
                            else:
                                return addnode([tree[0]] + tree[2:], a, b) + [tree[1]]
        self.__nodes = addnode(self.nodes() , x , y )
        return self

    def is_a_leaf(self, node):
        d = self.subtreey(node).nodes()
        if d[1] == []:
            return True
        else:
            return False


    def list_leaf(self):
        d = []
        for a in self.listnodess():
            if self.is_a_leaf(a):
                d += [a]
        return d

    def ancestor(self, y):
        def ancestorv(tree, a, x):
            if tree == []:
                return None
            else:
                if tree[0] == a:
                    return x
                else:
                    def localfunction(l, a):
                        if len(l) <= 1:
                            return None
                        else:
                            if ancestorv(l[1], a, l[0]) == None:
                                if len(l) < 3:
                                    return None
                                else:
                                    return ancestorv([l[0]] + l[2:], a, l[0])
                            else:
                                return ancestorv(l[1], a, l[0])
                    return localfunction(tree, a)
        return ancestorv(self.nodes() , y , self.nodes()[0])

    def is_root(tree, node):
        if tree.ancestor(node) == None:
            return False
        else:
            if tree.ancestor(node) == node:
                return True
            else:
                return False

    def commonancestor(self ,node1 , node2 ):
        if self.ancestor(node1) == self.ancestor(node2):
            return True
        else :
            return False

    #def one_way_to_root(self, identifiant):
        #if self.is_root(identifiant):
         #   return True
        #else:
         #   return self.one_way_to_root(self.ancestor(identifiant))

    #def one_and_only_root(self):
     #   d = 0
     #   for a in self.nodes().keys():
      #      if self.is_root(a):
       #         d += 1
        #if d == 1:
            #return True
       # else:
        #    return False

    #def well_formed(self):
     #   d = True
      #  for a in self.list_leaf():
       #     if self.one_and_only_root() and self.one_way_to_root(a):
        #        d = True and d
         #   else:
          #      d = False and d
        #return d


    def branch_level(self, node):
        if self.is_root(node):
            return 0
        else:
            return 1 + self.branch_level(self.ancestor(node))

    def list_of_node_at_level_n(self, n):
        d = []
        for a in self.listnodess():
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


    def auxdisplaytree(self):
        d = 0
        for i in  range(self.hauteur()+ 1 ):
            d = max(d , len(self.list_of_node_at_level_n(i)))
        return d

    def displaytree(self):
        def blankiterate(t , d):
            r =""
            for i in range(d - t ):
                r += " "
            return r
        n = Node("azertyuiop" , Node.BLOCK)
        y = ""
        for i in range(self.hauteur()+ 1 ):
            for j in range(len(self.list_of_node_at_level_n(i))):
                if self.commonancestor(n , self.list_of_node_at_level_n(i)[j]):
                    y += str(self.list_of_node_at_level_n(i)[j]) + "  "
                    n = self.list_of_node_at_level_n(i)[j]
                else :
                    y += "     " + str(self.list_of_node_at_level_n(i)[j]) + "     "
                    n = self.list_of_node_at_level_n(i)[j]
            print(blankiterate(len(self.list_of_node_at_level_n(i)) , self.auxdisplaytree()) + y + blankiterate(len(self.list_of_node_at_level_n(i)) , self.auxdisplaytree()) )
            y = ""
            n = Node("azertyuiop" , Node.BLOCK)

def blankiterate(t, d):
    r = ""
    for i in range(d - t):
        r += " "
    return r

"""print(blankiterate(4 , 8) + "1")





t = Tree([])
print(t.is_empty())


n = Node("e" ,Node.BLOCK)
v = Node("r" , Node.BLOCK)
y = Node("o" , Node.BLOCK)
m = Node("h" , Node.BLOCK)

t.addroot(n)
print(t.nodes())
t.addnod(v ,n)
print(t.nodes())
t.addnod(m , v)
t.addnod(y , v)
print(t.nodes())
print(t.ancestor(v).identifier())
print(t.root().identifier())
print(t.belongstotree(y))
print(t.is_root(n))
print(t.subtreey(v))
print(t.subtreey(v).listnodess())

print(t.auxdisplaytree())

t.displaytree()

print(t.list_of_node_at_level_n(2))"""
