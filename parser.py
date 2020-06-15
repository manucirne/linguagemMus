from rply import ParserGenerator
from AST import *
#referências:
#https://github.com/zjl233/moe/blob/master/src/parser.py
#https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df
#Ajuda do David para pensar o RETURN

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            ['NUM', 'PRINT', 'OPAREN', 'CPAREN',
             'FLINE', 'SUM', 'SUB', 'DIV', 'MULT',
              'AND', 'OR', 'OBLOCK', 'CBLOCK', 'OWHILE', 'CWHILE',
              'IF', 'ELSE', 'NOT', 'SAME', 'LESS', 'MORE', 'NOT', 'EQ',
              'VAR', 'INPUT','FUNC','VIRG', 'RETURN','TRUE', 'FALSE', 'FUNCC'],
            )

    def parse(self):
        
        @self.pg.production('program : commands')
        def program(p):
            return p[0]
        
        @self.pg.production('commands : command')
        def commandsunic(p):
            return Commands("",[p[0]])
        
        @self.pg.production('commands : commands command')
        def commandslist(p):
            p[0].chil.append(p[1])
            return p[0]
        
        @self.pg.production('command : funcassignment')
        @self.pg.production('command : assignment')
        @self.pg.production('command : printf')
        @self.pg.production('command : FLINE')
        @self.pg.production('command : whi')
        @self.pg.production('command : ifel')
        @self.pg.production('command : ret')
        @self.pg.production('command : funccall')
        def command(p):
            return p[0]
            
        @self.pg.production('printf : PRINT OPAREN relexp CPAREN FLINE')
        def printf(p):
            return Print("print",[p[2]])
        
        @self.pg.production('ret : RETURN relexp')
        def ret(p):
            return Return("RETURN",[p[1]])
            
        @self.pg.production('ret : RETURN')
        def retV(p):
            return Return("RETURN",[])
        
            
        @self.pg.production('whi : OWHILE OPAREN relexp CPAREN commands CWHILE')
        def whi(p):
            return Whi("while",[p[2],p[4]])
        
        @self.pg.production('ifel : IF OPAREN relexp CPAREN commands IF')
        @self.pg.production('ifel : IF OPAREN relexp CPAREN commands IF ELSE commands ELSE')
        def ifel(p):
            if len(p) > 7:
                return Ifel("if", [p[2],p[4],p[7]])
            else:
                return Ifel("if",[p[2],p[4]])
        
        @self.pg.production('assignment : VAR EQ relexp FLINE')
        def assignment(p):
            return Assig(p[0].value,[p[2]],"VAR",[])
        
        @self.pg.production('funcassignment : FUNC VAR param OBLOCK commands CBLOCK')
        def funcassignment(p):
            return Assig(p[1].value,[p[4]],"FUNC",p[2])
        
        @self.pg.production('funccall : FUNCC VAR paramcall FLINE')
        def funccall(p):
            return Fun(p[1].value,p[2])
        
        @self.pg.production('paramcall : OPAREN paramscall CPAREN')
        @self.pg.production('paramcall : OPAREN CPAREN')
        def paramcall(p):
            if len(p) > 2:
                return p[1]
            else:
                return []
        
        @self.pg.production('paramscall : relexp')
        def paramscall(p):
            return [p[0]]
        
        @self.pg.production('paramscall : paramscall VIRG relexp')
        def paramslistcall(p):
            p[0].append(p[2])
            return p[0]
        
        @self.pg.production('param : OPAREN params CPAREN')
        @self.pg.production('param : OPAREN CPAREN')
        def param(p):
            if len(p) > 2:
                return p[1]
            else:
                return []
        
        @self.pg.production('params : VAR')
        def params(p):
            return [p[0].value]
        
        @self.pg.production('params : params VIRG VAR')
        def paramslist(p):
            p[0].append(p[2].value)
            return p[0]
        
        @self.pg.production('relexp : expression')
        @self.pg.production('relexp : expression LESS expression')
        @self.pg.production('relexp : expression MORE expression')
        @self.pg.production('relexp : expression SAME expression')
        def relexp(p):
            if len(p) > 1:
                if p[1].gettokentype() == 'MORE':
                    return BinOp(">",[p[0],p[2]])
                elif p[1].gettokentype() == 'LESS':
                    return BinOp("<",[p[0],p[2]])
                elif p[1].gettokentype() == 'SAME':
                    return BinOp("==",[p[0],p[2]])
            else:
                return p[0]

        @self.pg.production('expression : term')
        @self.pg.production('expression : term SUM term')
        @self.pg.production('expression : term SUB term')
        @self.pg.production('expression : term AND term')
        @self.pg.production('expression : term OR term')
        def expression(p):
            if len(p) > 1:
                if p[1].gettokentype() == 'SUM':
                    return BinOp("+",[p[0],p[2]])
                elif p[1].gettokentype() == 'SUB':
                    return BinOp("-",[p[0],p[2]])
                elif p[1].gettokentype() == 'AND':
                    return BinOp("and",[p[0],p[2]])
                elif p[1].gettokentype() == 'OR':
                    return BinOp("or",[p[0],p[2]])
            else:
                return p[0]
        
        @self.pg.production('term : factor')    
        @self.pg.production('term : factor MULT factor')
        @self.pg.production('term : factor DIV factor')
        def term(p):
            if len(p) > 1:
                if p[1].gettokentype() == 'MULT':
                    return BinOp("*",[p[0],p[2]])
                elif p[1].gettokentype() == 'DIV':
                    return BinOp("//",[p[0],p[2]])
            else:
                return p[0]
            
        @self.pg.production('factor : NUM')
        @self.pg.production('factor : SUM NUM')
        @self.pg.production('factor : SUB NUM')
        @self.pg.production('factor : NOT NUM')
        @self.pg.production('factor : NOT TRUE')
        @self.pg.production('factor : NOT FALSE')
        @self.pg.production('factor : FUNCC VAR paramcall')
        @self.pg.production('factor : VAR')
        @self.pg.production('factor : OPAREN relexp CPAREN')
        @self.pg.production('factor : INPUT')
        @self.pg.production('factor : TRUE')
        @self.pg.production('factor : FALSE')
        def factor(p):
            if p[0].gettokentype() == 'NUM':
                return Num(p[0].value,[])
            elif len(p) == 3 and p[1].gettokentype() == 'VAR':
                return Fun(p[1].value,p[2])
            elif p[0].gettokentype() == 'SUM':
                return UnOp("+",[Num(p[1].value,[])])
            elif p[0].gettokentype() == 'SUB':
                return UnOp("-",[Num(p[1].value,[])])
            elif p[0].gettokentype() == 'NOT':
                if p[1].gettokentype() == 'NUM':
                    return UnOp("!",[Num(p[1].value,[])])
                elif p[1].gettokentype() == 'TRUE':
                    return UnOp("!",[BoolVal(True,[])])
                elif p[1].gettokentype() == 'FALSE':
                    return UnOp("!",[BoolVal(False,[])])
            elif p[0].gettokentype() == 'VAR':
                return Iden(p[0].value,[])
            elif p[0].gettokentype() == 'OPAREN':
                return p[1]
            elif p[0].gettokentype() == 'INPUT':
                return Input("",[p[0]])
            elif p[0].gettokentype() == 'TRUE':
                return BoolVal(True,[])
            elif p[0].gettokentype() == 'FALSE':
                return BoolVal(False,[])

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()