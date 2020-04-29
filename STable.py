class SymbleTable():
    
    def __init__(self):
        self.table = {}
        
    def Getter(self,var):
        try:
            res = self.table[var]
        except:
            raise Exception("Variável não existente")
        return res
        
    def Setter(self, var, value, tipo, param):
        self.table[var] = {}
        self.table[var]["value"] = value
        self.table[var]["tipo"] = tipo
        self.table[var]["param"] = param
        
    def findRet(self, i):
        return (i in self.table)