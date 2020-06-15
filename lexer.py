from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        # While
        self.lexer.add('OWHILE', r'\𝄆') # incio de repete é o início do while
        self.lexer.add('CWHILE', r'\𝄇') # fim do repete é o fim do while
        #If ELSE
        self.lexer.add('IF', r'\♪') # colcheia  é o if
        self.lexer.add('ELSE', r'\𝅘𝅥𝅯') # semicolcheia é o else
        # Function - coda marca um lugar que deve ser retomado quando necessário
        self.lexer.add('FUNC', r'\𝄋') # segno é a função
        self.lexer.add('FUNCC', r'\𝄉') # del segno é a chamada da função
        # virgula - a notação de respiração substitue a vírgual
        self.lexer.add('VIRG', r'\𝄒') #notação de respiração
        # Print - quando a música sai do papel
        self.lexer.add('PRINT', r'\🎙') # microfone é o print
        # Input - pauta - Quando a ideia vai pro papel
        self.lexer.add('INPUT', r'\🎼') # pauta com clave é o input
        # Parenthesis
        self.lexer.add('OPAREN', r'\(')
        self.lexer.add('CPAREN', r'\)')
        # block - A barra dupla marca o início e o fim de uma música
        self.lexer.add('OBLOCK', r'\𝄃') #barra dupla inicial
        self.lexer.add('CBLOCK', r'\𝄂') #barra dupla final
        # Semi Colon - a pausa de mínima marca um respiro maior, uma pausa para iniciar um novo pensamento
        self.lexer.add('FLINE', r'\𝄼') # pausa de mínima é o fim da linha
        # Operators - inspirados nos intervalos
        self.lexer.add('EQ', r'\♮') # bequadro é igual
        self.lexer.add('SUM', r'\♯') #sustenido é soma
        self.lexer.add('SUB', r'\♭') # bemol é o menos
        self.lexer.add('MULT', r'\𝄶') #oitava acima é o mult
        self.lexer.add('DIV', r'\𝄷') #oitava abaixo é o div
        #lógicos - inspirados em notações de interpretaçao (com excessão do and)
        self.lexer.add('AND', r'\𝅚') # cluster é o and - cluster é um acorde que junta notas de tons diferentes
        self.lexer.add('OR', r'\𝆖') # trêmulo é o or
        self.lexer.add('NOT', r'\𝆝') #ornamento é o not
        #COMPARATIVOS - inspirados em notações de interpretaçao
        self.lexer.add('LESS', r'\𝆒') #crescendo é o menor
        self.lexer.add('MORE', r'\𝆓') #decrescendo é o maior
        self.lexer.add('SAME', r'\𝄎') #repetição de compasso é o == 
        # Bool - inspirados em notações de interpretaçao
        self.lexer.add('TRUE', r'\𝆗') # turn é o true
        self.lexer.add('FALSE', r'\𝆘') # inverted turn é o false
        # Number
        self.lexer.add('NUM', '\d+')
        # return - segno marca um lugar importante da música o return faz o mesmo no código
        self.lexer.add('RETURN', '\𝄌') #coda é o return
        # Variables
        self.lexer.add('VAR', '[a-zA-Z][a-zA-Z0-9_]*')
        # Ignore spaces
        self.lexer.ignore(r'\s+')
        self.lexer.ignore(r'\\n+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
    