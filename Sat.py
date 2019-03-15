from Functionclass import *



class Connectorsbin(Enum):
    AND = 1
    OR = 2
    IMPLIES = 3
    EQUIV = 4

class Connectorsun(Enum):
    NEG = 5
    FORALL = 6
    EXISTS = 7





class Relationbinary(Enum):
    R = 1
    RSTAR = 2

class Relationunary(Enum):
    LABEL = 3
    VALUE = 4
    LABEL_TYPE = 5

class Mrelation(Enum):
    INF = 6
    SUP = 7
    EQ = 8
    INFOREQ = 9
    SUPOREQ = 10
    PLUS = 12
    MINUS = 13
    TIMES = 15
    CONCAT = 16

class Urelation(Enum):
    INTTOSTRING = 11

class Orelation(Enum):
    TRONC = 17





class Formulatomique():

    def __init__(self ):
        self.content = []

    def Getcontent(self):
        return self.content

    def GetRelationsOrConnectors(self):
        return type(self.content[0])

    def SortofRelationOrConnectors(self):
        return self.content[0]


    def MakeRFormula(self , x  , y  ):
        self.content = [Relationbinary.R , x , y ]

    def IsRFormula(self):
        return self.SortofRelationOrConnectors() == Relationbinary.R

    def MakeRStarFormula(self , x  , y  ):
        self.content = [Relationbinary.RSTAR , x , y ]

    def IsRStarFormula(self):
        return self.SortofRelationOrConnectors() == Relationbinary.RSTAR

    def MakeLabelFormula(self , x ):
        self.content = [Relationunary.LABEL , x ]

    def IsLabelFormula(self):
        return self.SortofRelationOrConnectors() == Relationunary.LABEL

    def MakeValueFormula(self , x ):
        self.content = [Relationunary.VALUE , x ]

    def IsValueFormula(self):
        return self.SortofRelationOrConnectors() == Relationunary.VALUE

    def MakeLabeltypeFormula(self , x ):
        self.content = [Relationunary.LABEL_TYPE , x ]


    def IsLabelTypeFormula(self):
        return self.SortofRelationOrConnectors() == Relationunary.LABEL_TYPE

    def MakeEqFormula(self, psi , phi ):
        self.content = [ Mrelation.EQ , psi , phi  ]

    def IsEqFormula(self):
        return self.SortofRelationOrConnectors() == Mrelation.EQ

    def MakeInfFormula(self, psi , phi ):
        self.content = [ Mrelation.INF , psi , phi  ]

    def IsInfFormula(self):
        return self.SortofRelationOrConnectors() == Mrelation.INF

    def MakeSupFormula(self, psi , phi ):
        self.content = [ Mrelation.SUP , psi , phi  ]

    def IsSupFormula(self):
        return self.SortofRelationOrConnectors() == Mrelation.SUP

    def MakeInfEqFormula(self, psi , phi ):
        self.content = [ Mrelation.INFOREQ , psi , phi  ]

    def IsInfOrEqFormula(self):
        return self.SortofRelationOrConnectors() == Mrelation.INFOREQ

    def MakeSupEqFormula(self, psi , phi ):
        self.content = [ Mrelation.SUPOREQ, psi , phi  ]

    def IsSupOrEqFormula(self):
        return self.SortofRelationOrConnectors() == Mrelation.SUPOREQ

    def MakePlusFormula(self, psi , phi ):
        self.content = [ Mrelation.PLUS , psi , phi  ]

    def IsPlusFormula(self):
        return self.SortofRelationOrConnectors() == Mrelation.PLUS

    def MakeTimesFormula(self, psi , phi ):
        self.content = [ Mrelation.TIMES , psi , phi  ]

    def IsTimesFormula(self):
        return self.SortofRelationOrConnectors() == Mrelation.TIMES

    def MakeMinusFormula(self, psi , phi ):
        self.content = [ Mrelation.MINUS , psi , phi]

    def IsMinusFormula(self):
        return self.SortofRelationOrConnectors() == Mrelation.MINUS

    def MakeConcatFormula(self, psi , phi ):
        self.content = [ Mrelation.CONCAT , psi , phi  ]

    def IsConcatFormula(self):
        return self.SortofRelationOrConnectors() == Mrelation.PLUS

    def MakeInttostringFormula(self, psi):
        self.content = [ Urelation.INTTOSTRING , psi  ]

    def IsIntToStringFormula(self):
        return self.SortofRelationOrConnectors() == Urelation.INTTOSTRING

    def MakeTroncFormula(self, psi , x , y   ):
        self.content = [ Orelation.TRONC  , psi , x , y   ]

    def IsTroncFormula(self):
        return self.SortofRelationOrConnectors() == Orelation.TRONC

    def MakeAndFormula(self, psi , phi ):
        self.content = [ Connectorsbin.AND , psi , phi  ]

    def ReMakeAndFormula(self , psi):
        empty = Formulatomique()
        empty.MakeAndFormula(self , psi)

    def IsAndFormula(self):
        return self.SortofRelationOrConnectors() == Connectorsbin.AND

    def MakeOrFormula(self, psi , phi ):
        self.content = [ Connectorsbin.OR , psi , phi  ]

    def IsOrFormula(self):
        return self.SortofRelationOrConnectors() == Connectorsbin.OR

    def MakeEquivFormula(self, psi , phi ):
        self.content = [ Connectorsbin.EQUIV , psi , phi  ]

    def IsEquivFormula(self):
        return self.SortofRelationOrConnectors() == Connectorsbin.EQUIV


    def MakeImpliesFormula(self, psi , phi ):
        self.content = [ Connectorsbin.IMPLIES , psi , phi ]

    def IsImpliesFormula(self):
        return self.SortofRelationOrConnectors() == Connectorsbin.IMPLIES

    def MakeNegFormula(self, psi  ):
        self.content = [ Connectorsun.NEG , psi  ]

    def IsNegFormula(self):
        return self.SortofRelationOrConnectors() == Connectorsun.NEG

    def MakeExistsFormula(self , psi , x ):
        self.content  = [Connectorsun.EXISTS , x , psi ]

    def IsExitsFormula(self):
        return self.SortofRelationOrConnectors() == Connectorsun.EXISTS

    def MakeForallFormula(self , x , psi  ):
        self.content = [Connectorsun.FORALL , x ,  psi ]

    def IsForallFormula(self):
        return self.SortofRelationOrConnectors() == Connectorsun.FORALL

    def MinimalFormula(self):
        return self.GetRelationsOrConnectors() == Relationbinary or  self.GetRelationsOrConnectors() == Relationunary

    def MinBinFormula(self):
        return  self.GetRelationsOrConnectors() == Relationbinary

    def MinUnFormula(self):
        return self.GetRelationsOrConnectors() == Relationunary

    def UnaryFormula(self):
        return self.GetRelationsOrConnectors() == Connectorsun or self.GetRelationsOrConnectors() == Urelation

    def BinaryFormula(self):
        return self.GetRelationsOrConnectors() == Connectorsbin or self.GetRelationsOrConnectors() == Mrelation

    def TriFormula(self):
        return self.GetRelationsOrConnectors() == Orelation

    def SetContent1(self , b):
        self.content[1] = b

    def SubstitutionUnary(self , x , y  ):
        if self.Getcontent()[1] == x :
            self.content[1] = y

    def SubstitutionBinary(self , x , y ):
        if self.Getcontent()[1] == x :
            self.content[1] = y
        if self.Getcontent()[2] == x :
            self.content[2] = y


    def RecSubstitutionBinary(self , x , y  ):
        self.content[1].Substitution(x , y )
        self.content[2].Substitution(x , y)

    def RecSubstituionUnary(self , x , y):
        self.content[1].Substitution(x , y)

    def RecSubstitutionTrinary(self , x , y):
        self.content[3].Substitution(x, y)


    def Substitution(self , x  , y):
        if self.MinBinFormula():
            self.SubstitutionBinary(x ,y)
        if self.MinUnFormula():
            self.SubstitutionUnary(x , y)
        if self.UnaryFormula():
            self.RecSubstituionUnary(x ,y )
        if self.BinaryFormula():
            self.RecSubstitutionBinary(x ,y )
        if  self.TriFormula():
            self.RecSubstitutionTrinary(x ,y )

    def EvalValue(self):
        return self.Getcontent()[1].GetValue()

    def EvalLabel(self):
        return self.Getcontent()[1].GetLabel()

    def EvalLabelType(self):
        return self.Getcontent()[1].GetLabelType()

    def EvalIntToString(self):
        return str( self.Getcontent()[1].Evaluation() )

    def PlusEvalutation(self):
        return self.Getcontent()[1].Evaluation() + self.Getcontent()[2].Evaluation()

    def MinusEvalutation(self):
        return self.Getcontent()[1].Evaluation() - self.Getcontent()[2].Evaluation()

    def TimesEvalutation(self):
        return self.Getcontent()[1].Evaluation() * self.Getcontent()[2].Evaluation()

    def EqEvaluation(self):
        return self.Getcontent()[1].Evaluation() == self.Getcontent()[2].Evaluation()

    def SupEvaluation(self):
        return self.Getcontent()[1].Evaluation() > self.Getcontent()[2].Evaluation()

    def InfEvaluation(self):
        return self.Getcontent()[1].Evaluation() < self.Getcontent()[2].Evaluation()

    def SupOrEqEvaluation(self):
        return self.Getcontent()[1].Evaluation() >= self.Getcontent()[2].Evaluation()

    def InfOrEqEvaluation(self):
        return self.Getcontent()[1].Evaluation() <= self.Getcontent()[2].Evaluation()

    def ConcatEvaluation(self):
        return self.Getcontent()[1].Evaluation() + self.Getcontent()[1].Evaluation()

    def TroncEvaluation(self):
        return (self.Getcontent()[3].Evalution())[self.Getcontent()[1], self.Getcontent()[2]]


    def Evaluation(self):
        if self.IsPlusFormula():
            return  self.PlusEvalutation()
        if self.IsMinusFormula():
            return self.MinusEvalutation()
        if self.IsTimesFormula():
            return self.TimesEvalutation()
        if self.IsConcatFormula():
            return self.ConcatEvaluation()
        if self.IsEqFormula():
            return self.EqEvaluation()
        if self.IsSupFormula():
            return self.SupEvaluation()
        if self.IsSupOrEqFormula():
            return self.SupOrEqEvaluation()
        if self.IsInfFormula():
            return  self.InfEvaluation()
        if self.IsInfOrEqFormula():
            return self.InfOrEqEvaluation()
        if self.IsLabelFormula():
            return self.EvalLabel()
        if self.IsValueFormula():
            return self.EvalValue()
        if self.IsLabelTypeFormula():
            return self.IsLabelTypeFormula()
        if self.IsIntToStringFormula():
            return self.EvalIntToString()
        if self.IsTroncFormula():
            return self.TroncEvaluation()













class Nodes():

    def __init__(self , value , label , label_type):
        self.value = value
        self.label = label
        self.label_type = label_type
        self.pathfromroot = []


    def GetValue(self):
        return self.value

    def SetValue(self , value ):
        self.value = value

    def GetLabel(self):
        return self.label

    def SetLabel(self , label ):
        self.label = label

    def GetLabelType(self):
        return self.label_type

    def SetLabelType(self , label_type):
        self.label_type = label_type

    def GetPathFromRoot(self):
        return self.pathfromroot

    def SetPathFromRoot(self , path):
        self.pathfromroot = path

    def ChangingPrefixPath(self , path1 , path2):
        l = len(path1)
        self.pathfromroot = path2 + self.pathfromroot[l : ]

    def Copy(self):
        j = self.GetPathFromRoot()
        t = self.GetLabel()
        d = self.GetValue()
        r = self.GetLabelType()
        n = Nodes( d , t , r )
        n.SetPathFromRoot(j)
        return n

    def CopyPath(self):
        j = self.GetPathFromRoot()
        return j

    def PathLabel(self):
        l = []
        for a in self.pathfromroot :
            l += [a.GetLabel()]
        return l









n = Nodes(None , "toto" , "block")
m = Nodes(None , "gamma" , "block")
z = Nodes( 40 , "integer" , "olaf")












class Tree():

    def __init__(self):
        self.nodes = []
        self.edges = []

    def GetListNodes(self):
        return self.nodes


    def AddRoot(self , root):
        if not self.GetListNodes() == []:
            raise ValueError
        root.SetPathFromRoot([root])
        self.nodes = [root]

    def IsRoot(self , node):
        return  len(node.GetPathFromRoot()) == 1

    def NodesInTree(self , x ):
        return x in self.GetListNodes()

    def AddEdge(self , couple ):
        x , y  = couple
        if not self.NodesInTree(x):
            raise ValueError
        path = x.GetPathFromRoot() + [y]
        y.SetPathFromRoot(path)
        self.nodes += [y]
        self.edges += [couple]

    def GetAncestor(self ,x):
        if self.IsRoot(x):
            raise ValueError
        else :
            l = len(x.GetPathFromRoot())
            l -= 1
            return x.GetPathFromRoot()[-2 ]

    def IsAncestor(self , x , y  ):
        if not ( self.NodesInTree(x) and self.NodesInTree(y)):
            raise ValueError
        return self.GetAncestor(y) == x

    def IsAncestorTransitiveClosure(self , x , y):
        if not ( self.NodesInTree(x) and self.NodesInTree(y)):
            raise ValueError
        return  x in y.GetPathFromRoot()

    def GetEdges(self):
        return self.edges

    def GetNodeFromPath(self , path):
        for a in self.GetListNodes():
            if a.GetPathFromRoot() == path:
                return a

    def RemoveEdges(self , node):
        self.nodes.remove(node)
        for a in self.edges:
            if a[1] == node :
                self.edges.remove(a)
            if a[0] == node:
                self.edges.remove(a)
                self.RemoveEdges( a[1])


    def AddEdgeViaChangingPrefixPath(self , path1 , path2 , node ):
        node.ChangingPrefixPath(path1 , path2)
        a = self.GetAncestor(node)
        self.edges += [( a ,node )]
        self.nodes += [node]

    def GetEdgesFromNode(self , node , l ):
        for a in self.edges:
            if a[0] == node :
                l += [a[1]]
        return l

    def Nextnodes(self , node):
        return self.GetEdgesFromNode(node , [])





    def NextPath(self , path1 ):
        h = []
        x = self.GetNodeFromPath(path1 )
        l = self.Nextnodes( x  )
        for a in l:
            h += [a.GetPathFromRoot()]
        return h






    def NextPath2(self , path , l ):
        for a in self.NextPath(path):
            l += self.NextPathFinal(a)
        return l


    def NextPathFinal(self , path ):
        return self.NextPath2(path , self.NextPath(path))


    def AuxNextPathLabel(self , listepath ):
        h = []
        for a in listepath :
            l = []
            for b in a:
                l += [b.GetLabel()]
            h += [l]
        return h

    def NextPathLabel(self , path ):
        return self.AuxNextPathLabel( self.NextPathFinal(path ) )



    def FunctionNewBlock(self , path , label ):
        j = Nodes(  None , label , "block")
        n = self.GetNodeFromPath(path)
        path += [j]
        j.SetPathFromRoot(path)
        self.nodes += [j]
        self.edges += [(n ,j )]
        return self

    def FunctionNewVar(self , path , label , label_type , value):
        j = Nodes(  value , label , label_type )
        n = self.GetNodeFromPath(path)
        path += [j]
        j.SetPathFromRoot(path)
        self.nodes += [j]
        self.edges += [(n ,j )]
        return self

    def FunctionDelete(self , path  ):
        n = self.GetNodeFromPath(path)
        self.RemoveEdges(n)
        return self


    def FunctionTest(self  , condition ):
        Saaat = Satisfaction(self, condition)
        return Saaat.Sat()



    def FunctionMove(self , path1 , path2):
        self.FunctionSend(path1 , path2)
        self.FunctionDelete(path1)
        return self

    def AuxSend(self , path1 , path2 ):
        n = self.GetNodeFromPath(path1)
        j = n.Copy()
        x = self.GetNodeFromPath(path2)
        path3 = path2 + [j]
        j.SetPathFromRoot(path3)
        self.nodes += [j]
        self.edges += [(x, j)]

    def Aux2Send(self, path1 , path2 , l  ):
        for a in l:
            t = self.GetNodeFromPath(a)
            j = t.Copy()
            self.AddEdgeViaChangingPrefixPath(path1 , path2 , j)
            print(j.PathLabel())


    def FunctionSend(self , path1 , path2):
        l = self.NextPathFinal(path1)
        self.AuxSend(path1 , path2 )
        self.Aux2Send(path1 , path2 + [path1[-1]] , l  )
        return self


    def FunctionSet(self , path1 , value):
        n = self.GetNodeFromPath(path1)
        n.SetValue( value)
        return self

    def IsBBlock(self , path ):
        n = self.GetNodeFromPath(path)
        if n.GetLabel() == "block":
            return True
        else :
            return False

    def AddConstant(self , path , value):
        n = self.GetNodeFromPath(path)
        n.SetValue(value + n.GetValue())

    def AddNodeToNodeValue(self , path1 , path2 ):
        n = self.GetNodeFromPath(path1)
        h = self.GetNodeFromPath(path2)
        n.SetValue(n.GetValue() + h.GetValue())

    def SubConstant(self , path , value):
        n = self.GetNodeFromPath(path)
        n.SetValue( n.GetValue() - value)

    def SubNodeToNodeValue(self , path1 , path2 ):
        n = self.GetNodeFromPath(path1)
        h = self.GetNodeFromPath(path2)
        n.SetValue(n.GetValue() - h.GetValue())

    def MulNodeToNodeValue(self , path1 , path2 ):
        n = self.GetNodeFromPath(path1)
        h = self.GetNodeFromPath(path2)
        n.SetValue(n.GetValue() * h.GetValue())

    def MulConstant(self , path , value):
        n = self.GetNodeFromPath(path)
        n.SetValue(value * n.GetValue())

    def DivNodeToNodeValue(self , path1 , path2 ):
        n = self.GetNodeFromPath(path1)
        h = self.GetNodeFromPath(path2)
        n.SetValue(n.GetValue() / h.GetValue())

    def DivConstant(self , path , value):
        n = self.GetNodeFromPath(path)
        n.SetValue(n.GetValue() / value )


    def ListeLabelNode(self):
        l = []
        for a in self.GetListNodes():
            l +=  [a.GetLabel()]
        return l

    def ListePathLabelNode(self):
        l = []
        for a in self.GetListNodes():
            l +=  [a.GetPathFromRoot()]
        return self.AuxNextPathLabel( l )


    def apply(self , function ):
        if function.IsNewBFunction():
            if function.IsAtomicFunction():
                return self.FunctionNewBlock(function.GetDestinationPathNewBlock() , function.GetLabelNewBlock() )
            else :
                return (self.apply(function.NextFunction())).FunctionNewBlock(function.GetDestinationPathNewBlock() , function.GetLabelNewBlock() )
        if function.IsNewVFunction():
            if function.IsAtomicFunction():
                return self.FunctionNewVar(function.GetDestinationPathNewVar() , function.GetLabelNewVar() , function.GetLabelTypeNewVar() , function.GetValueNewvar() )
            else :
                return (self.apply( function.NextFunction())).FunctionNewVar(function.GetDestinationPathNewVar() , function.GetLabelNewVar() , function.GetLabelTypeNewVar() , function.GetValueNewvar() )
        if function.IsMoveFunction():
            if function.IsAtomicFunction():
                return self.FunctionMove(function.GetCurrentPathMove(), function.GetDestinationPathMove()   )
            else :
                return (self.apply(function.Nextfunction())).FunctionMove(function.GetCurrentPathMove(), function.GetDestinationPathMove()   )
        if function.IsSendFunction():
            if function.IsAtomicFunction():
                return  self.FunctionSend(function.GetCurrentPathSend() , function.GetDestinationPathSend())
            else :
                return (self.apply(function.NextFunction())).FunctionSend(function.GetCurrentPathSend() , function.GetDestinationPathSend())
        if function.IsDeleteFunction():
            if function.IsAtomicFunction():
                return self.FunctionDelete(function.GetCurrentPath() )
            else :
                return (self.apply(function.NextFunction())).FunctionDelete(function.GetCurrentPath() )
        if function.IsSetFunction():
            if function.IsAtomicFunction():
                return  self.FunctionSet( function.GetCurrentPathSet() , function.GetValueSet())
            else :
                return (self.apply( function.NextFunction() )).FunctionSet( function.GetCurrentPathSet() , function.GetValueSet())



h = Nodes( 6 , "r" , "t" )
t = Nodes( 3 , "e" , "ty")
x = Nodes( 4 , "go" , "lo")
tree = Tree()
tree.AddRoot(n)
tree.AddEdge((n , m))
tree.AddEdge((m , z))
tree.AddEdge( (m ,h) )










g = Functions()
f = Functions()
f.makeNewBlockFunction(None , "Jasmine" ,  [n,m ,h ])
g.MakeSendFunction(f , [n , m ] , [ n  , m   ] )



tree.apply(g)

print(tree.ListePathLabelNode())









































class Satisfaction():

    def __init__(self , tree , formula ):
        self.tree = tree
        self.formula = formula
        self.bool = True

    def GetFormula(self):
        return self.formula

    def GetTree(self):
        return self.tree



    def GetContFormula(self):
        z = self.GetFormula()
        return z.Getcontent()

    def AtomiqueSat(self):
        phi = self.GetFormula()
        self.bool = phi.Evaluation()
        return self.bool

    def RSat(self):
        phi = self.GetContFormula()
        tree = self.GetTree()
        x = phi[1]
        y = phi[2]
        return tree.IsAncestor(x ,y)

    def RStarSat(self):
        phi = self.GetContFormula()
        tree = self.GetTree()
        x = phi[1]
        y = phi[2]
        return tree.IsAncestorTransitiveClosure(x ,y)

    def AndSat(self):
        Sat1 = Satisfaction(tree , self.GetContFormula()[1])
        Sat2 = Satisfaction(tree , self.GetContFormula()[2])
        return Sat1.Sat() and Sat2.Sat()

    def OrSat(self):
        Sat1 = Satisfaction(tree , self.GetContFormula()[1])
        Sat2 = Satisfaction(tree , self.GetContFormula()[2])
        return Sat1.Sat() or Sat2.Sat()

    def NegSat(self):
        Sat1 = Satisfaction(tree, self.GetContFormula()[1])
        return not Sat1.Sat()

    def EquivSat(self):
        Sat1 = Satisfaction(tree, self.GetContFormula()[1])
        Sat2 = Satisfaction(tree, self.GetContFormula()[2])
        return (not (Sat1.Sat()) or  Sat2.Sat()  ) and  ( not (Sat2.Sat()) or Sat1.Sat() )

    def ImpliesSat(self):
        Sat1 = Satisfaction(tree, self.GetContFormula()[1])
        Sat2 = Satisfaction(tree, self.GetContFormula()[2])
        return not(Sat1.Sat()) or Sat2.Sat()

    def SubstitutionSat(self , x , y  ):
        phi = self.GetFormula()
        phi.Substitution(x , y )
        Sat1 = Satisfaction(self.GetTree() , phi )
        return Sat1.Sat()

    def ExistSat(self):
        p = False
        var = self.GetContFormula()[1]
        for y in self.GetListNodes():
            p = p or self.SubstitutionSat(var , y )
        return p

    def ForallSat(self):
        p = True
        var = self.GetContFormula()[1]
        for y in self.GetListNodes():
            p = p and self.SubstitutionSat(var, y)
        return p

    def Sat(self):
        phi = self.GetFormula()
        if phi.IsAndFormula():
            return self.AndSat()
        if phi.IsOrFormula():
            return self.OrSat()
        if phi.IsNegFormula():
            return self.IsNegFormula()
        if phi.IsImpliesFormula():
            return self.ImpliesSat()
        if phi.IsEquivFormula():
            return  self.EquivSat()
        if phi.IsRFormula():
            return self.RSat()
        if phi.IsRStarFormula():
            return self.RStarSat()
        if phi.IsExistFormula():
            return self.ExistSat()
        if phi.IsForallFormula():
            return self.ForallSat()
