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
   'COMANDOCONDICIONAL',
   'ELSE',
   'LBRACKET',
   'RBRACKET',
   'AND',
   'OR',
   'MOD',
   'GT',
   'LT',
   'DIF',
   'DIVISION',
   'MULTIPLICATION',
   'PLUS',
   'MINUS',
   'MATHEQUALS',
   'COMMA',
   'FOR',
   'IN',
   'RANGE',
   'WHILE',
   'TRUE',
)

reserved = {
   'int' : 'INT',
   'float' : 'FLOAT',
   'str' : 'STR',
   'print' : 'PRINT',
   'for':'FOR',
   'in':'IN',
   'range':'RANGE',
   'while':'WHILE',
   'True':'TRUE',
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
t_DIVISION = r'/'
t_MULTIPLICATION = r'\*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_OR = r'or'
t_MOD = r'mod'
t_MATHEQUALS = r'=='
t_FOR = r'for'
t_IN = r'in'
t_RANGE = r'range'
t_WHILE = r'while'
t_TRUE = r'True'
t_COMMA = r','

#CONDICIONAIS
t_IF = r'if'

def t_COMANDOCONDICIONAL(t):
    r'if\((.*?)\)'
    return t

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
    t.value = str(t.value[1:-1])  # remove single quotes
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

lexer.input("""for int a in range(1,10){
                    print(a)
                }
                for int a in range(1, 10, 5){
                    print(a)
                }
                while(True){
                    print("a")
                }
                while(a==b){
                    print("a igual a b")
                }
            """)

while True:
    tok = lexer.token()
    if not tok: 
        break      
    print(tok)
    with open('Trabalho_Pratico/lexico/repeticao.txt', 'a') as f:
      f.write(str(tok) + '\n')