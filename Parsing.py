import os
from algebraicprocess import Tree,Node,Formula,Connectors,Relations



def is_empty(file):
    if os.path.getsize(file) == 0:
        return True
    else :
        return False




def allowed_word(identifiant):
    if identifiant == "block" or identifiant == "end" or identifiant == "port":
        return False
    else:
        return True

"""def rebuilt_file(liste , file ):
    f = open(file , w)
    f.write(" ")
    f.close()
    f = open(file , a )
    for b in liste:
        f.write(b + "  ")
    f.close()"""

def get_chaine(file):
    if is_empty(file):
        print("no word in an empty file")
    else :
        f = open(file , "r" )
        chaine = f.readline()
        d = chaine
        while chaine != "":
            chaine = f.readline()
            d += " " + chaine
        f.close()
        return d.split()

def get_el(liste):
    if liste ==[] :
        return None
    else :
        u = liste[0]
        liste.remove(liste[0])
        return u



def parse_end(liste , tree , current_node):
    if liste == [] :
        return tree
    else :
        x = get_el(liste)
        print(x)
        if not allowed_word(x):
            current_node = tree.ancestor(current_node)
            print(tree.nodes())
            if x == "block":
                return parse_block(liste, tree, current_node)
            elif x == "end":
                return parse_end(liste , tree , current_node)
            else:
                return parse_port(liste, tree, current_node)
        else:
            print(" not a well formed model")


def parse_block(liste, tree , current_node):
    if liste == []:
        print("not a well formed model")
    else :
        b = get_el(liste)
        print(b)
        if allowed_word(b):
            if current_node == None :
                tree.addroot(b)
                current_node = b
                print(tree.nodes())
                if liste == []:
                    print("not a well formed model")
                else:
                    x = get_el(liste)
                    print(x)
                    if allowed_word(x):
                        print("not a well formed model")
                    else:
                        if x == "block":
                            return parse_block(liste, tree , current_node)
                        elif x == "end" :
                            return parse_end(liste ,tree , current_node)
                        else :
                            return parse_port(liste , tree , current_node)
            else :
                tree.addnod(b, current_node)
                current_node = b
                print(tree.nodes())
                if liste == []:
                    print("not a well formed model")
                else:
                    x = get_el(liste)
                    print(x)
                    if allowed_word(x):
                        print("not a well formed model")
                    else:
                        if x == "block":
                            return parse_block(liste, tree , current_node)
                        elif x == "end" :
                            return parse_end(liste ,tree , current_node)
                        else :
                            return parse_port(liste , tree , current_node)
        else:
            print("not a well formed model")

def parse_port(liste , tree , current_node):
    if liste == []:
        print("not a well formed model")
    else :
        p = get_el(liste)
        print(p)
        if allowed_word(p):
            tree.addnod(p , current_node)
            print(tree )
            if liste == []:
                print("not a well formed model")
            else:
                x = get_el(liste)
                print(x)
                print(liste)
                print(current_node)
                print(tree.is_root("System"))
                print(allowed_word(x))
                print(x == "end")
                if allowed_word(x):
                    print("not a well formed model")
                else:
                    if x == "block":
                        return parse_block(liste, tree , current_node)
                    elif x == "end":
                        return parse_end(liste ,tree , current_node)
                    else :
                        return parse_port(liste , tree , current_node)
        else:
            print("not a well formed model ")


def parser(file):
    liste = get_chaine(file)
    if liste == [] :
        t = Tree([])
        return t
    else :
        x = get_el(liste)
        if x == "block":
            t = Tree([])
            current_node = None
            return  parse_block(liste , t , current_node )
        else :
            print( " not a well formed model")


l = parser("ex3")
print(l.nodes())

def fonctor( l , t , j ):
    if not t == 0:
        if l[0] == "end":
            t -= 1
            j += [l[0]]
        if l[0] == "block":
            t += 1
            j += [l[0]]
        else :
            j += [l[0]]
        return fonctor(l[:1] , t , j)
    else :
        if l[0] == "end":
            return  j
        if l[0] == "block" :
            t += 1
            j += [l[0]]
            return fonctor(l[:1] , t , j)
        else :
            j += [l[0]]
            return fonctor(l[:1], t, j)






def proj1(x):
    if not x[0] == "block" :
        raise ValueError
    else:
        return [x[2]] + fonctor(x[:3] , 0 , [])

def proj2(x):
    lastel = proj1(x)[-1]
    i = proj1(x).index(lastel) + 1
    return  x[:i]




def ParseAnd(x,  formula , y ) :
    if y == 1 :
        formula[1] = [Connectors.AND , subParser(proj1(x) , formula , 1) , subParser(proj2(x) , formula , 2) ]
    if y == 2 :
        formula[2] = [Connectors.AND , subParser(proj1(x) , formula , 1) , subParser(proj2(x) , formula , 2) ]
    else :
        raise ValueError
    return formula

def ParseOr(x,  formula , y ) :
    if y == 1 :
        formula[1] = [Connectors.OR , subParser(proj1(x) , formula , 1) , subParser(proj2(x) , formula , 2) ]
    if y == 2 :
        formula[2] = [Connectors.OR ,subParser(proj1(x) , formula , 1) , subParser(proj2(x) , formula , 2) ]
    else :
        raise ValueError
    return formula


def ParseImplies(x,  formula , y ) :
    if y == 1 :
        formula[1] = [Connectors.IMPLIES , subParser(proj1(x) , formula , 1) , subParser(proj2(x) , formula , 2) ]
    if y == 2 :
        formula[2] = [Connectors.IMPLIES , subParser(proj1(x) , formula , 1) , subParser(proj2(x) , formula , 2)]
    else :
        raise ValueError
    return formula

def ParseEquiv(x,  formula , y ) :
    if y == 1 :
        formula[1] = [Connectors.EQUIV, subParser(proj1(x) , formula , 1) , subParser(proj2(x) , formula , 2) ]
    if y == 2 :
        formula[2] = [Connectors.EQUIV , subParser(proj1(x) , formula , 1) , subParser(proj2(x) , formula , 2) ]
    else :
        raise ValueError
    return formula

def ParseNeg(x,  formula , y ) :
    if y == 1 :
        formula[1] = [Connectors.NEG , subParser(proj1(x) , formula , 1)  ]
    if y == 2 :
        formula[2] = [Connectors.NEG , subParser(proj1(x) , formula , 1)  ]
    else :
        raise ValueError
    return formula

def ParseExists(x , formula , y ):
    if y == 1 :
        formula[1] = [Connectors.EXIST , proj1(x) , subParser(proj1(x) , formula , 1) ]
    if y == 2 :
        formula[2] = [Connectors.EXIST , proj1(x) , subParser(proj1(x) , formula , 1) ]
    else :
        raise ValueError
    return formula

def ParseForall(x , formula , y ):
    if y == 1 :
        formula[1] = [Connectors.EXIST , proj1(x) , subParser(proj1(x) , formula , 1) ]
    if y == 2 :
        formula[2] = [Connectors.EXIST , proj1(x) , subParser(proj1(x) , formula , 1) ]
    else :
        raise ValueError
    return formula

def ParseR(x , formula , y):
    if y == 1 :
        formula[1] = [Relations.R , x[1] , x[2]]
    if y == 2 :
        formula[2] = [Relations.R , x[1] , x[2]]
    else :
        raise ValueError
    return formula

def ParseO(x , formula , y ):
    if y == 1 :
        formula[1] = [Relations.O , x[1] , x[2]]
    if y = 2 :
        formula[2] = [Relations.O , x[1] , x[2]]
    else :
        raise ValueError
    return formula

def ParseLabel(x , formula , y):
    if y == 1 :
        formula[1] = [Relations.LABEL , x[1] , x[2]]
    if y == 2 :
        formula[2] = [Relations.LABEL , x[1] , x[2]]
    else :
        raise ValueError
    return formula

def ParseValue(x , formula , y):
    if y == 1 :
        formula[1] = [Relations.VALUE, x[1] , x[2]]
    if y == 2 :
        formula[2] = [Relations.VALUE , x[1] , x[2]]
    else :
        raise ValueError
    return formula

def ParseBlock(x ,formula , y):
    if y == 1 :
        formula[1] = [Relations.BlOCK , x[1]]
    if y == 2 :
        formula[2] = [Relations.BlOCK , x[1]]
    else :
        raise ValueError
    return formula

def subParser( x  , formula , y ):
    if not x[0] == "block":
        raise ValueError
    else :
        if x[1] == "AND":
            ParseAnd(x , formula , y)
        if x[1] == "OR" :
            ParseOr(x , formula , y)
        if x[1] == "IMPLIES":
            ParseImplies(x , formula , y )
        if x[1] == "EQUIV" :
            ParseEquiv( x ,formula ,y )
        if x[1] == "EXIST":
            ParseExists(x , formula , y )
        if x[1] == "FORALL":
            ParseForall(x , formula , y )
        if x[1] == "R":
            ParseR(x , formula , y )
        if x[1] == "O":
            ParseO(x , formula , y )
        if x[1] == "LABEL":
            ParseLabel(x , formula , y )
        if x[1] == "VALUE":
            ParseValue(x , formula  ,y)
        if x[1] == "BLOCK":
            ParseBlock(x ,formula , y )
        if x[1] == "NEG":
            ParseNeg(x , formula , y )
        else :
            raise ValueError

def ParserFormul(x):
    if not x[0] == "block":
        raise ValueError
    else :
        if x[1] == "R":
            return [Relations.R , x[1] , x[2]]
        if x[1] == "O":
            return [Relations.O , x[1] , x[2]]
        if x[1] == "LABEL":
            return [Relations.LABEL , x[1] , x[2]]
        if x[1] == "VALUE":
            return [Relations.VALUE , x[1] , x[2]]
        if x[1] == "BLOCK":
            return  [Relations.BlOCK , x[1]]
        else :
            if x[1] == "AND":
                return subParser(proj2(x ) , subParser(proj1(x) , [Connectors.AND , [] , [] ] , 1 ) , 2)
            if x[1] == "OR":
                return subParser(proj2(x ) , subParser(proj1(x) , [Connectors.OR , [] , [] ] , 1 ) , 2)
            if x[1] == "IMPLIES":
                return subParser(proj2(x ) , subParser(proj1(x) , [Connectors.OR , [] , [] ] , 1 ) , 2)
            if x[1] == "EQUIV":
                return subParser(proj2(x ) , subParser(proj1(x) , [Connectors.EQUIV , [] , [] ] , 1 ) , 2)
            if x[1] == "NEG":
                return  subParser(proj1(x) , [Connectors.NEG , [] ] , 1 )


def parseFormula(file):
    return ParserFormul(get_chaine(file))


