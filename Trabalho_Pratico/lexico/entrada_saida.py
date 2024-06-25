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
   'INPUT'  
)

reserved = {
   'int' : 'INT',
   'float' : 'FLOAT',
   'str' : 'STR',
   'print' : 'PRINT',
   'input' : 'INPUT'
}

t_EQUALS    = r'='
t_LPAREN    = r'\('
t_RPAREN    = r'\)'

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
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

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ID(t):
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
            str c = input()
            print(a)
            print('teste')
            print("teste")""")

while True:
    tok = lexer.token()
    if not tok: 
        break      
    print(tok)
    with open('Trabalho_Pratico/lexico/entrada_saida.txt', 'a') as f:
      f.write(str(tok) + '\n')