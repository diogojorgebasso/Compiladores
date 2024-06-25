import ply.yacc as yacc

import sys
sys.path.insert(0, 'D:/code/Compiladores/Trabalho_Pratico/lexico')

from repeticao import tokens

#define o programa
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
    '''statement : for_statement
                 | while_statement
                 | print_statement
                 | assignment_statement'''
    p[0] = p[1]

def p_assignment_statement(p):
    '''assignment_statement : ID EQUALS condition NEWLINE'''
    p[0] = f"{p[1]} = {p[3]}"

#ATTENTION --
def p_condition(p):
    '''condition : expression comparison_operator expression
                 | condition logical_operator condition
                 | ID comparison_operator ID'''
    if len(p) == 4:
        p[0] = f"{p[1]} {p[2]} {p[3]}"
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
                     | FOR INT ID IN RANGE LPAREN NUMBER COMMA NUMBER RPAREN LBRACKET NEWLINE assignment_statement RBRACKET NEWLINE
                     | FOR INT ID LBRACKET NEWLINE statement_list RBRACKET NEWLINE'''
    if len(p) == 18:
        p[0] = f"for {p[3]} in range({p[7]}, {p[9]}, {p[11]}):\n{indent(p[15])}"
    elif len(p) == 16:
        p[0] = f"for {p[3]} in range({p[7]}, {p[9]}):\n{indent(p[13])}"
    else:
        p[0] = f"for {p[3]} in {p[5]}:\n{indent(p[6])}"

def p_while_statement(p):
    '''while_statement : WHILE LPAREN condition RPAREN LBRACKET NEWLINE statement_list RBRACKET NEWLINE
                       | WHILE LPAREN TRUE RPAREN LBRACKET NEWLINE statement_list RBRACKET NEWLINE'''
    p[0] = f"while({p[3]}):\n{indent(p[7])}"

def p_print_statement(p):
    '''print_statement : PRINT LPAREN ID RPAREN NEWLINE
                       | PRINT LPAREN STRING RPAREN NEWLINE'''
    p[0] = f'print({p[3]})\n'

def indent(code_block, level=1):
    indentation = '    '  # 4 spaces
    if isinstance(code_block, list):
        code_block = "\n".join(code_block)
    else:  # Handle other types gracefully
        code_block = str(code_block)
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
data = '''for int a in range(1,10){ 
    a = a*2
}
while(True){
    print("Hello World")
}
while(d>b and a!=b){ 
    print(a) 
}
'''

result = parser.parse(data)
code_to_execute = ''.join(result)
print(code_to_execute)
# escrevendo para um arquivo específico
with open('Trabalho_Pratico/sintatico/repeticao/output.txt', 'w') as file:
    file.write(code_to_execute)

print("Compilado com sucesso!")
#executando o código no próprio script    
exec(code_to_execute)
