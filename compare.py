from assoctable import Assoctable
from arbreetnoueuds import Tree, Node



def associatethings(l1 , l2 , assoct , l , i ):
    if l1 == []:
        return (i ,l )
    else :
        if l2 == []:
            l += l1
            return (i , l )
        else:
            a = assoct.getassociate(l1[0] , l2)
            if not a == None:
                l2.remove(a)
                i += [(l1[0] , a)]
                return  associatethings(l1[1:] , l2 , assoct , l , i)
            else:
                l += [l1[0]]
                return associatethings(l1[1:] , l2 , assoct , l , i )


table = Assoctable()
table.addclasse([1 , 6 ,7])
table.addclasse( [2 , 11] )
table.addclasse( [5 , 10])
print(table.getassociate( 1 , [6 , 7 , 8 , 9  , 10 , 11 , 12 , 13 ] ))

print( associatethings([1 , 2 , 3 , 4 , 5 ] , [6 , 7 , 8 , 9  , 10 , 11 , 12 , 13 ]  , table  , [] , [] ))
print(table.classes())
print( associatethings([6 , 7 , 8 , 9  , 10 , 11 , 12 , 13 ] , [1 , 2 , 3 , 4 , 5 ]  , table  , [] , [] ))


def diffandsim(l1 , l2 , assoct ):
    j , k = l1.copy() ,l2.copy()
    v , b = l1.copy() ,l2.copy()
    table = assoct
    toble = assoct
    y ,z  = associatethings(j ,k , table , [] , []  )
    u, t =  associatethings(b, v , toble , [] , [])
    p = (z , t)
    return (y , p)


print( diffandsim([1 , 2 , 3 , 4 , 5 ] , [6 , 7 , 8 , 9  , 10 , 11 , 12 , 13 ]  , table ) )

n = Node("e" , Node.BLOCK )



t = Tree([])



def compare(la , ld , file  , assoct , tree1 , tree2 ):
    if file == []:
        return (la , ld )
    else :
        x,z = file[0]
        if tree1.is_a_leaf(x) :
            ld += tree2.subtreey(z).listnodess()[1:]
            return compare(la , ld , file[1:] , assoct , tree1 , tree2)
        else :
            if tree2.is_a_leaf(z):
                ld += tree1.subtreey(x).listnodess()[1:]
                return compare(la, ld, file[1:], assoct, tree1, tree2)
            else :
                l1 = x.children()
                l2 = z.children()
                i , l = diffandsim(l1 , l2 , assoct , [] , [] )
                la += i
                ld += l
                return compare(la , ld , i + file[1:] , assoct , tree1 , tree2)


def comparaison(tree1 , tree2 , assoctab):
    x1 = tree1.root()
    x2 = tree2.root()
    liste1 = x1.children()
    liste2 = x2.children()
    la , ld = diffandsim(liste1 , liste2 , assoctable )
    return compare(la ,ld , la , assoctab , tree1 , tree2)
