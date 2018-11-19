class assoctable:
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
        if self.classes() == []:
            print( " not in the list ")
        else:
            if a in self.classes()[0]:
                return self.classes()[0]
            else:
                self.__classes = self.__classes[1:]
                return self.getclas(a)

    def assoclist(self , lis):
        if lis == []:
            return []
        else:
            return self.getclas(lis[0]) + self.assoclist(lis[1:])

    def getassociate(self , a , l2):
        l = self.getclas(a)
        if l2 ==[]:
            return None
        else :
            if  l == self.getclas(l[0]):
                return l[0]
            else:
                return self.getassociate( a  , l2[1:])
