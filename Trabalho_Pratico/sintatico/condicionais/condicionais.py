import ply.yacc as yacc

import sys
sys.path.insert(0, 'D:/code/Compiladores/Trabalho_Pratico/lexico')

from repeticao import tokens

def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : declaration
                 | assignment
                 | print_statement
                 | conditional_statement'''
    p[0] = p[1]

def p_declaration(p):
    '''declaration : type ID EQUALS expression NEWLINE'''
    p[0] = ('declaration', p[1], p[2], p[4])

def p_assignment(p):
    '''assignment : ID EQUALS expression NEWLINE'''
    p[0] = ('assignment', p[1], p[3])

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN NEWLINE'''
    p[0] = ('print', p[3])

def p_conditional_statement(p):
    '''conditional_statement : IF LPAREN condition RPAREN LBRACKET statement_list RBRACKET
                             | IF LPAREN condition RPAREN LBRACKET statement_list RBRACKET ELSE LBRACKET statement_list RBRACKET'''
    if len(p) == 8:
        p[0] = ('if', p[3], p[6])
    else:
        p[0] = ('if-else', p[3], p[6], p[11])

def p_condition(p):
    '''condition : expression comparator expression
                 | expression comparator expression AND condition
                 | expression comparator expression OR condition'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    else:
        p[0] = (p[2], p[1], p[3], p[4], p[5])

def p_comparator(p):
    '''comparator : GT
                  | LT
                  | DIF
                  | MATHEQUALS'''
    p[0] = p[1]

def p_type(p):
    '''type : INT
            | FLOAT
            | STR'''
    p[0] = p[1]

def p_expression(p):
    '''expression : NUMBER
                  | FNUMBER
                  | STRING
                  | ID'''
    p[0] = p[1]

def p_error(p):
    print("Erro sintático no '%s' na linha %d" % (p.value, p.lineno))

parser = yacc.yacc()

data = """int a = 5
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
            """

result = parser.parse(data)
print(result)