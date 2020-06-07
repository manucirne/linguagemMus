from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # While
        self.lexer.add('OWHILE', r'\𝄆') # incio de repete é o início do while
        self.lexer.add('CWHILE', r'\𝄇') # fim do repete é o fom do while
        #For
        self.lexer.add('FOR', r'\𝄎') #repetidor de compasso é o for
        #If ELSE
        self.lexer.add('IF', r'\♪') # colcheia  é o if
        self.lexer.add('ELSE', r'\𝅘𝅥𝅯') # semicolcheia é o else
        # Function
        self.lexer.add('FUNC', r'\𝄌') # coda é a função
        # virgula
        self.lexer.add('VIRG', r'\,')
        # Print
        self.lexer.add('PRINT', r'\𝄞') # clave de sol é o input
        # Input
        self.lexer.add('INPUT', r'\𝄢') # clave de fá é o input
        # Parenthesis
        self.lexer.add('OPAREN', r'\(')
        self.lexer.add('CPAREN', r'\)')
        # block
        self.lexer.add('OBLOCK', r'\{')
        self.lexer.add('CBLOCK', r'\}') 
        # Semi Colon
        self.lexer.add('FLINE', r'\𝄼') # pausa de mínima é o fim da linha
        # Operators
        self.lexer.add('EQ', r'\♮') # bequadro é igual
        self.lexer.add('SUM', r'\♯') #sharp é soma
        self.lexer.add('SUB', r'\♭') # flat é o menos
        self.lexer.add('MULT', r'\𝄰') #sharp up é o mult
        self.lexer.add('DIV', r'\𝄭') #flat down é o div
        self.lexer.add('AND', r'\𝆑') # forte é o and
        self.lexer.add('OR', r'\𝆐') #mezzo é o or
        self.lexer.add('NOT', r'\𝆍') #subto é o not
        #COMPARATIVOS
        self.lexer.add('LESS', r'\𝆒') #crescendo é o menor
        self.lexer.add('MORE', r'\𝆓') #decrescendo é o maior
        self.lexer.add('SAME', r'\𝆌') #Rinforzando é o == 
        # Bool
        self.lexer.add('TRUE', r'\𝆗') # volta é o true
        self.lexer.add('FALSE', r'\𝆘') # invertida é o false
        # Number
        self.lexer.add('NUM', '\d+')
        # return
        self.lexer.add('RETURN', '\𝄋') #duas colcheias é o return
        # Variables
        self.lexer.add('VAR', '[a-zA-Z][a-zA-Z0-9_]*')
        # Ignore spaces
        self.lexer.ignore(r'\s+')
        self.lexer.ignore(r'\\n+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
    