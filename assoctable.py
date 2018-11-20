class Assoctable:
    def __init__(self):
        self.__classes = []

    def classes(self):
        return self.__classes

    def addclasse(self , classe ):
        self.__classes += [classe]

    def addelem(self , classe  , a ):
        if classe in self.classes():
            self.__classes.remove(classe)
            self.__classes += [classe + [a]]

    def getclas(self , a ):
        def getc(l ,a ):
            if l == []:
                return [a]
            else:
                if a in l[0]:
                    return l[0]
                else:
                    return getc(l[1:] , a )
        i = self.classes()
        return getc(i , a)

    def assoclist(self , lis):
        if lis == []:
            return []
        else:
            return self.getclas(lis[0]) +  self.assoclist(lis[1:])

    def getassociate(self , a , l2):
        l = self.getclas(a)
        if l2 ==[]:
            return None
        else :
            if  l == self.getclas(l2[0]):
                return l2[0]
            else:
                return self.getassociate( a  , l2[1:])
