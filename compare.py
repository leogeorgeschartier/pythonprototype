def associatethings(l1 , l2 , assoct , l , i ):
    if l1 == []:
        l += l2
        return ( i , l )
    else :
        if l2 == []:
            l += l1
            return (i , l)
        else:
            if l1[0] in assoct.assoclist(l2):
                a = assoct.getassociate(l1[0] , l2)
                l2.remove(a)
                i += [(l1[0] , a)]
                return  associatethings(l1[1:] , l2 , assoct , l , i)
            else:
                l += [l1[0]]
                return associatethings(l1[1:] , l2 , assoct , l , i )


def compare(l1 , l2 , assoct , tree1 , tree2 , l ):
    y ,z  = associatethings(l1 , l2 , assoct , [] , []  )
    if y == []:
        return l
    else :
        if tree1.is_a_leaf( y[0][0]):
            return tree2.subtreey(y[0][1])
