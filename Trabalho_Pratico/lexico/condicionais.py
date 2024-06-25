import ply.lex as lex

#data type: int, float, str
#actual values: number, fnumber, string

tokens = (
   'INT', 
   'FLOAT',
   'STR',
   'PRINT',
   'ID',
   'EQUALS',
   'NUMBER',
   'FNUMBER',
   'STRING',
   'NEWLINE',
   'LPAREN',
   'RPAREN',
   'IF',
   'ELSE',
   'LBRACKET',
   'RBRACKET',
   'AND',
   'OR',
   'GT',
   'LT',
   'DIF',
   'MATHEQUALS',
)

reserved = {
   'int' : 'INT',
   'float' : 'FLOAT',
   'str' : 'STR',
   'print' : 'PRINT',
   'if': 'IF'
}

t_EQUALS    = r'='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'
t_LBRACKET  = r'\{'
t_RBRACKET  = r'\}'

#Mathematical operators
t_GT = r'>'
t_LT = r'<'
t_DIF = r'!='
t_OR = r'or'
t_MATHEQUALS = r'=='

#CONDICIONAIS
t_IF = r'if'


def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

def t_AND(t):
    r'and'
    #t.value = Boolean(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FNUMBER(t):
    r'[+-]?\d+\.\d+'
    t.value = float(t.value)
    return t

def t_STRING(t):
    r'\".*?\"|\'.*?\''
    t.value = str(t.value)  
    return t

def t_ELSE(t):
    r'else'
    return t

def t_ID(t): #tem que ser o último
    r'\w+'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

t_ignore  = ' \t' #ignore espaços e tabs

def t_error(t):
    print("Caractere ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

lexer.input("""int a = 5
            float b = -5.1
            int c = 6
            if(b==a and c>b){
                print("a igual a b")
            }
            if(a>b){
                print("a maior que b")
            }else{
                print("b maior que a")
            }

            """)

while True:
    tok = lexer.token()
    if not tok: 
        break      
    print(tok)
    with open('Trabalho_Pratico/lexico/condicionais.txt', 'a') as f:
      f.write(str(tok) + '\n')


