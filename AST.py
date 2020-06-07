from STable import SymbleTable

class Node():
    def __init__(self,value, chil):
        self.value = value
        self.chil = chil
    
    def eval(self,table):
        pass

class Commands(Node):
    def eval(self,table):
        for i in self.chil:
            i.eval(table)
            if table.findRet("RETURN"):
                return table.Getter("RETURN")["value"]
            

class Num(Node):
    def eval(self, table):
        return int(self.value)

class UnOp(Node):
    def eval(self,table):
        if self.value == "+":
            return + self.chil[0].eval(table)
        elif self.value == "-":
            return - self.chil[0].eval(table)
        elif self.value == "!":
            return  not self.chil[0].eval(table)
        
class Assig(Node):
    def __init__(self, value, chil, tipo, param):
        self.tipo = tipo
        self.param = param
        self.chil = chil
        self.value = value
        
    def eval(self,table):
        if self.tipo == "FUNC":
            table.Setter(self.value,self.chil[0], self.tipo, self.param)

        else:
            table.Setter(self.value,self.chil[0].eval(table), self.tipo, self.param)
        
class Iden(Node):
        
    def eval(self,table):
        return table.Getter(self.value)["value"]
    
class Return(Node):
    def eval(self,table):
        if len(self.chil) > 0:
            table.Setter(self.value,self.chil[0].eval(table),"","")
        else:
            table.Setter(self.value,None,"","")

class Fun(Node):
    def __init__(self,value,param):
        self.param = param
        self.value = value
        
    def eval(self,table):
        st = SymbleTable()
        res = table.Getter(self.value)
        for p in range(len(self.param)):
            st.Setter(res["param"][p],self.param[p].eval(table),"VAR","")
        code = res["value"].eval(st)
        return code
     
class Ifel(Node):
        
    def eval(self,table):
        if self.chil[0].eval(table) == True:
            self.chil[1].eval(table)
        elif len(self.chil) == 3:
            self.chil[2].eval(table)
            
class Whi(Node):
        
    def eval(self,table):
        while self.chil[0].eval(table) == True:
            self.chil[1].eval(table)
            
class BinOp(Node):
        
    def eval(self,table):
        if self.value == "+":
            return self.chil[0].eval(table) + self.chil[1].eval(table)
        elif self.value == "-":
            return self.chil[0].eval(table) - self.chil[1].eval(table)
        elif self.value == "*":
            return self.chil[0].eval(table) * self.chil[1].eval(table)
        elif self.value == "//":
            return self.chil[0].eval(table) // self.chil[1].eval(table)
        elif self.value == "or":
            return self.chil[0].eval(table) or self.chil[1].eval(table)
        elif self.value == "and":
            return self.chil[0].eval(table) and self.chil[1].eval(table)
        elif self.value == ">":
            return self.chil[0].eval(table) > self.chil[1].eval(table)
        elif self.value == "<":
            return self.chil[0].eval(table) < self.chil[1].eval(table)
        elif self.value == "==":
            return self.chil[0].eval(table) == self.chil[1].eval(table)

class Print(Node):
    def eval(self, table):
        print(self.chil[0].eval(table))
        
class Input(Node):      
    def eval(self,table):
        return int(input())