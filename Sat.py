from enum import Enum

class Connectors(Enum):
    AND = 1
    OR = 2
    NEG = 3
    IMPLIES = 4
    EQUIV = 5
    EXIST = 6
    FORALL = 7

class Relations(Enum):
    R = 1
    O = 2
    VALUE = 3
    LABEL= 4
    BlOCK = 5


class Node():

    def __init__(self, value , label , blockport):
        self.__value = value
        self.__label  = label
        self.__block = blockport


    def Value(self):
        return self.__value

    def Label(self):
        return self.__label

    def Isblock(self):
        return self.__block


class Tree:

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

n = Node(5 , "carburant" , False  )
v = Node(6 , "carburant" , False )
y = Node(None , None , False  )
m = Node(None  , None , False )

t = Tree([])

t.addroot(n)
print(t.nodes())
t.addnod(v ,n)
print(t.nodes())
t.addnod(m , v)
t.addnod(y , v)
print(t.listnodess())
print(t.ancestor(v).Value())
print(t.root().Value())
print(t.belongstotree(y))
print(t.is_root(n))
print(t.subtreey(v))


class Formula():

    def __init__(self , rel , x , y ):
        if not type(rel) == Relations:
            raise ValueError
        else :
            if y == None :
                self.content = [rel , x]
            else:
                self.content = [rel , x , y ]

    def makeAnd(self , formula):
        self.content = [Connectors.AND , self.content , formula.content ]

    def makeOr(self , formula):
        self.content = [Connectors.OR , self.content , formula.content ]

    def makeImplies(self , formula):
        self.content = [Connectors.IMPLIES , self.content , formula.content ]

    def makeEquiv(self , formula):
        self.content = [Connectors.EQUIV, self.content , formula.content  ]

    def makeNeg(self ):
        self.content = [Connectors.NEG, self.content ]

    def makeExists(self , x ):
        self.content =  [Connectors.EXIST , x , self.content  ]

    def makeForall(self , x ):
        self.content = [Connectors.FORALL, x, self.content]

phi = Formula(Relations.BlOCK , 1 , None )
psi = Formula(Relations.R , 1 , 2 )

phi.makeAnd(psi )
phi.makeExists(1)
phi.makeExists(2)

print(phi.content)






def sigma(v , y , c ):
    if type(v[0]) == Connectors :
        if v[0] == Connectors.EXIST or v[0] == Connectors.FORALL:
            v[2] = sigma(v[2], y, c)
        else:
            v[1] = sigma( v[1] , y , c )
            v[2] = sigma( v[2] , y , c )
    else :
        if v[0] == Relations.BlOCK:
            if v[1] == y :
                v[1] = c
        else :
            if v[1] == y :
                v[1] = c
            else :
                if v[2] == y :
                    v[2] = c
                else :
                    v = v
    return v



h = Node(None , None , True)
g = Node( 5 , "e" , False )

f = Tree([])
f.addroot(h)
f.addnod(g,h)
print(f.belongstotree(n))

print(sigma(phi.content , 1 , h ))


def sat(tree1 , formula):
    def modelato(arbre , v):
        if v[0] == Relations.R:
            if arbre.belongstotree(v[1]) and arbre.belongstotree(v[2]):
                if arbre.ancestor(v[2] ) == v[1]:
                    return True
                else :
                    return False
            else :
                raise ValueError
        if v[0] == Relations.O:
            if arbre.belongstotree(v[1]) and arbre.belongstotree(v[2]):
                if arbre.ontheleft(v[1] , v[2] ):
                    return True
                else:
                    return False
            else :
                raise ValueError
        if v[0] == Relations.VALUE:
            if arbre.belongstotree(v[1]) and arbre.belongstotree(v[2]):
                if v[1].Value() == v[2]:
                    return True
                else :
                    return False
            else :
                raise  ValueError
        if v[0] == Relations.LABEL :
            if arbre.belongstotree(v[1]) and arbre.belongstotree(v[2]):
                if v[1].Label() == v[2]:
                    return True
                else :
                    return False
            else :
                raise ValueError
        if v[0] == Relations.BlOCK :
            if arbre.belongstotree(v[1]) :
                if v[1].Isblock():
                    return True
                else :
                    return False
            else :
                raise  ValueError
        else :
            raise ValueError
    def models(tree , v ):
        p = False
        r = True
        if v[0] == Connectors.AND :
            return models(tree , v[1] ) and models(tree , v[2] )
        if v[0] == Connectors.OR :
            return models(tree , v[1]) or models( tree , v[2])
        if v[0] == Connectors.NEG :
            return not models(tree , v[1])
        if v[0] == Connectors.IMPLIES :
            return models(tree , v[2]) or not models(tree , v[1])
        if v[0] == Connectors.EQUIV :
            return models(tree , [Connectors.IMPLIES ,  v[1] , v[2] ]) and models(tree , [Connectors.IMPLIES ,  v[1] , v[2]] )
        if v[0] == Connectors.EXIST :
            for i in tree.listnodess():
                p = p or models(tree , sigma( v[2] , v[1] , i ))
            return p
        if v[0] == Connectors.FORALL :
            for i in tree.listnodess():
                r = r and models(tree , sigma( v[2] , v[1] , i ))
            return r
        else :
            return modelato( tree , v )
    return models(tree1 , formula.content)

print(sat(f , phi ))
print(sat(f,psi))
print(psi.content )
