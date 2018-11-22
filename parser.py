import os
from arbreetnoueuds import Tree,Node



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

def rebuilt_file(liste , file ):
    f = open(file , w)
    f.write(" ")
    f.close()
    f = open(file , a )
    for b in liste:
        f.write(b + "  ")
    f.close()

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
l.displaytree()

vb = parser("ex4" )
vb.displaytree()
