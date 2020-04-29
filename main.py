from preProcess import Preprocess
from lexer import Lexer
from parser import Parser
from STable import SymbleTable
import sys

# 𝄌 ♫  ♪   𝅘𝅥𝅯    ♯  ♭  𝄰  ♮  𝄭  𝄆  𝄇 inicio e fim de bloco que se repete  𝄌  𝄎 repete  𝄔  𝄕  pausas: 𝄽   𝄾   𝄼 
# 𝆑 forte  𝆐 mezzo  𝆍 subto  𝆌 Rinforzando  𝄞  𝄢  𝄭  𝄈  𝆒 crescendo  𝆓 decrescebdo 𝆗 turn  𝆘 inverted turn

def main(s1):
    file_in = s1
    code = ""
    if file_in[-5:] == ".song":
        with open(file_in,"r") as f:
            for line in f: 
                code += line

    ppro = Preprocess(code)
    clean = ppro.Removecomm()

    ST = SymbleTable()
    lexer = Lexer().get_lexer()
    tokens = lexer.lex(clean)
        
    pg = Parser()
    pg.parse()
    parser = pg.get_parser()
    r = parser.parse(tokens)
    r.eval(ST)
    
main(sys.argv[1])