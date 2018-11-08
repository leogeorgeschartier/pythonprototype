import os


def is_empty(file):
    if os.path.getsize(file) == 0:
        return True
    else :
        return False




def allowed_word(identifiant):
    if identifant == "block" or identifiant == "end" or identifiant == "port":
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

def get_word(file):
    if is_empty(file):
        print("no word in an empty file")
    else :
        f = open(file , r )
        chaine = f.readline()
        while chaine != "":
            chaine += " " + f.readline()
        rebuilt_file(chaine.split()[1:] , f)
        f.close()
        return chaine.split()[0]

def parse_end(file , tree , current_node):
    if is_empty_file(file):
        return tree
    else :
        if tree.is_root(current_node):
            return tree
        elif tree.is_root(tree.ancestor(current_node)):
            x = get_word(file)
            if not allowed_word(x):
               tree.add_node(x , c)
               current_node = tree.ancestor(current_node)
               if x == "block":
                   return parse_block(file , tree , current_node)
               elif x == "end":
                   return tree
               else :
                   return parse_port(file , tree , current_node)
            else :
                print(" not a well formed model")
        else :
            x = get_word(file)
            if not allowed_word(x):
                tree.add_node(x, c)
                current_node = tree.ancestor(current_node)
                if x == "block":
                    return parse_block(file, tree, current_node)
                elif x == "end":
                    return parse_end(file , tree , current_node)
                else:
                    return parse_port(file, tree, current_node)
            else:
                print(" not a well formed model")


def parse_block(file , tree , current_node):
    if is_empty(file):
        print("not a well formed model")
    else :
        b = get_word(file)
        if allowed_word(b):
            if current_node == None :
                tree.add_node(b)
                current_node = b
            else :
                tree.add_node(b , current_node)
                current_node = b
                if is_empty_file:
                    print("not a well formed model")
                else:
                    x = get_word(file)
                    if allowed_word(x):
                        print("not a well formed model")
                    else:
                        if x == "block":
                            parse_block(file, tree , current_node)
                        elif x == "end" :
                            parse_end(file ,tree , current_node)
                        else :
                            parse_port(file , tree , current_node)

def parse_port(file , tree , current_node):
    if is_empty(file):
        print("not a well formed model")
    else :
        p = get_word(file)
        if allowed_word(p):
            tree.add_node(p , current_node)
            if is_empty_file:
                print("not a well formed model")
            else:
                x = get_word(file)
                if allowed_word(x):
                    print("not a well formed model")
                else:
                    if x == "block":
                        parse_block(file, tree , current_node)
                    elif x == "end" :
                        parse_end(file ,tree , current_node)
                    else :
                        parse_port(file , tree , current_node)


def parser(file):
    if is_empty(file):
        t = tree()
        return t
    else :
        if x == "block":
            t = tree()
            current_node = None
            return parse_block(file , t , current_node )
        else :
            print( " not a well formed model")
