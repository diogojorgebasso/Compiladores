import ply.yacc as yacc

import sys
sys.path.insert(0, 'D:/code/Compiladores/Trabalho_Pratico/lexico')

from repeticao import tokens

#define o programa
def p_program(p):
    '''program : statement_list'''
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement NEWLINE
                      | statement_list statement NEWLINE'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : for_statement
                 | while_statement
                 | print_statement
                 | assignment_statement'''
    p[0] = p[1]

def p_assignment_statement(p):
    '''assignment_statement : ID EQUALS condition'''
    p[0] = ('assign', p[1], p[3])

def p_condition(p):
    '''condition : expression comparison_operator expression
                 | condition logical_operator condition
                 | TRUE
                 | FALSE'''
    if len(p) == 4:
        p[0] = (p[2], p[1], p[3])
    elif len(p) == 5:
        p[0] = (p[2], p[1], p[3], p[4])
    else:
        p[0] = p[1]

def p_comparison_operator(p):
    '''comparison_operator : LT
                           | GT
                           | PLUS
                           | MATHEQUALS
                           | DIF'''
    p[0] = p[1]

def p_expression(p):
    '''expression : NUMBER
                  | STRING
                  | ID'''
    p[0] = p[1]

def p_logical_operator(p):
    '''logical_operator : AND
                        | OR'''
    p[0] = p[1]


def p_for_statement(p):
    '''for_statement : FOR INT ID IN RANGE LPAREN NUMBER COMMA NUMBER COMMA NUMBER RPAREN LBRACKET NEWLINE statement_list RBRACKET NEWLINE
              | FOR INT ID IN RANGE LPAREN NUMBER COMMA NUMBER RPAREN LBRACKET NEWLINE statement_list RBRACKET NEWLINE
              | FOR INT ID IN ID LBRACKET statement_list RBRACKET NEWLINE'''
    if len(p) == 15:  # for int a in range(1,2,3)
        p[0] = ('for', p[3], p[7], p[9], p[11], p[13])
    elif len(p) == 13:  # for int b in range(1,2)
        p[0] = ('for', p[3], p[7], p[9], None, p[11])
    else:  # for int a in b
        p[0] = ('for', p[3], p[5], None, None, p[7])

def p_while_statement(p):
    '''while_statement : WHILE LPAREN condition RPAREN LBRACKET NEWLINE statement_list RBRACKET NEWLINE'''
    p[0] = ('while', p[3], p[6])

def p_print_statement(p):
    '''print_statement : PRINT LPAREN ID RPAREN NEWLINE
                       | PRINT LPAREN STRING RPAREN NEWLINE'''
    p[0] = ('print', p[3])

def indent(code_block, level=1):
    indentation = '    '  # 4 spaces
    if isinstance(code_block, list):
        code_block = "\n".join(code_block)
    indented_code = ''.join(f"{indentation*level}{line}\n" for line in code_block.splitlines())
    return indented_code

# Error rule for syntax errors
def p_error(p):
    if p:
        print("Erro sintático no '%s' na linha %d" % (p.value, p.lineno))
    else:
        print("Erro sintático no final do arquivo")

# Build the parser
parser = yacc.yacc()

# Test it out
data = '''for int a in range(1, 10){ 
            b = b + a
          }
          while(True){
            print("Hello World")
          }
          while(d>b and a!=b){ 
            print(a) 
          }
          '''

result = parser.parse(data)

print(result)