# linguagemMus

Para rodar crie um arquivo .song que siga a ebnf documentada abaixo. Depois use o esse arquivo como argumento.
Exemplo:

> python3 main.py arquivo_criado.song

## EBNF:

>PROGRAM = { COMMAND } ;
>
>COMMAND = (( λ | ASSIGNMENT | PRINT | FUNCCALL | RETURN ), "𝄼 ") | WHILE | IF | FUNCASSIG | COMMENT;
>
>ASSIGNMENT = IDENTIFIER, "♮", RELEXP;
>
>PRINT = "🎙", EXPRESSION ;
>
>WHILE = "𝄆", "(", RELEXP, ")", CODE, "𝄇";
>
>IF = ("♪", "(", RELEXP, ")", BLOCK, "♪") | ("♪", "(", COND, ")", BLOCK, "♪", "𝅘𝅥𝅯 ", CODE, "𝅘𝅥𝅯 ");
>
>FUNCASSIG = "𝄋", "𝄃", VAR, "(", PARAMASSIG, ")", BLOCK, "𝄂";
>
>PARAMCALL = [ RELEXP { "," RELEXP } ] ;
>
>PARAMASSIG = [ IDENTIFIER { "," IDENTIFIER } ] ;
>
>RETURN = "𝄌" , [RELEXP], "𝄼 "
>
>RELEXP = EXPRESSION , { ("𝄎" | "𝆓" | "𝆒"), EXPRESSION } ;
>
>EXPRESSION = TERM, { ("♯" | "♭" | "𝆖"), TERM } ;
>
>TERM = FACTOR, { ("𝄶" | "𝄷" | "𝅚 "), FACTOR } ;
>
>FACTOR = (("♯" | "♭" | "𝆝"), FACTOR) | NUMBER | (𝄋 IDENTIFIER "(" PARAMCALL ")" ) | "(", RELEXP, ")" | IDENTIFIER | INPUT ;
>
>INPUT = "🎼" ;
>
>IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
>
>NUMBER = DIGIT, { DIGIT } ;
>
>LETTER = ( a | ... | z | A | ... | Z ) ;
>
>DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
>
>COMMENT = "𝄾 ",{*}; 


