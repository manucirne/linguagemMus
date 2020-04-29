from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # While
        self.lexer.add('OWHILE', r'\𝄆')
        self.lexer.add('CWHILE', r'\𝄇')
        #For
        self.lexer.add('FOR', r'\𝄎')
        #If ELSE
        self.lexer.add('IF', r'\♪')
        self.lexer.add('ELSE', r'\𝅘𝅥𝅯')
        # Function
        self.lexer.add('FUNC', r'\𝄌')
        # virgula
        self.lexer.add('VIRG', r'\,')
        # Print
        self.lexer.add('PRINT', r'\𝄞')
        # Input
        self.lexer.add('INPUT', r'\𝄢')
        # Parenthesis
        self.lexer.add('OPAREN', r'\(')
        self.lexer.add('CPAREN', r'\)')
        # block
        self.lexer.add('OBLOCK', r'\{')
        self.lexer.add('CBLOCK', r'\}')
        # Semi Colon
        self.lexer.add('FLINE', r'\𝄼')
        # Operators
        self.lexer.add('EQ', r'\♮')
        self.lexer.add('SUM', r'\♯')
        self.lexer.add('SUB', r'\♭')
        self.lexer.add('MULT', r'\𝄰')
        self.lexer.add('DIV', r'\𝄭')
        self.lexer.add('AND', r'\𝆑')
        self.lexer.add('OR', r'\𝆐')
        self.lexer.add('NOT', r'\𝆍')
        #COMPARATIVOS
        self.lexer.add('LESS', r'\𝆒')
        self.lexer.add('MORE', r'\𝆓')
        self.lexer.add('SAME', r'\𝆌')
        # Bool
        self.lexer.add('TRUE', r'\𝆗')
        self.lexer.add('FALSE', r'\𝆘')
        # Number
        self.lexer.add('NUM', '\d+')
        # return
        self.lexer.add('RETURN', '\♫')
        # Variables
        self.lexer.add('VAR', '[a-zA-Z][a-zA-Z0-9_]*')
        # Ignore spaces
        self.lexer.ignore(r'\s+')
        self.lexer.ignore(r'\\n+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
    