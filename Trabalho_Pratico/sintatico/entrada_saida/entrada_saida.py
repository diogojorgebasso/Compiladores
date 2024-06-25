import ply.yacc as yacc

import sys
sys.path.insert(0, 'D:/code/Compiladores/Trabalho_Pratico/lexico')

from entrada_saida import tokens

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
                 | print_statement'''
    p[0] = p[1]

def p_declaration(p):
    '''declaration : type ID EQUALS expression NEWLINE'''
    p[0] = f"{p[2]} = {p[4]}\n"

def p_print_statement(p):
    '''print_statement : PRINT LPAREN ID RPAREN NEWLINE
                       | PRINT LPAREN STRING RPAREN NEWLINE'''
    if p[3].startswith(("'", '"')):  # If it's a string literal
        p[0] = f'print({p[3]})\n'  # Keep the quotes
    else:  # It's an identifier
        p[0] = f'print({p[3]})\n'  # No need to add quotes, corrected logic

def p_type(p):
    '''type : INT
            | FLOAT
            | STR'''
    p[0] = p[1]

def p_expression(p):
    '''expression : NUMBER
                  | FNUMBER
                  | STRING
                  | ID
                  | input_call'''
    p[0] = p[1]

def p_input_call(p):
    '''input_call : INPUT LPAREN RPAREN
                  | INPUT LPAREN STRING RPAREN'''
    if len(p) == 4:  # Matches input()
        p[0] = "input()"
    else:  # Matches input("some string")
        p[0] = f'input({p[3]})'

def p_error(p):
    print("Erro sintático no '%s' na linha %d" % (p.value, p.lineno))

parser = yacc.yacc()

data = """int a = 5
float b = -5.1
str c = input("digite o numero")
print(a)
print('teste')
print("teste")
            """

result = parser.parse(data)
code_to_execute = ''.join(result)
# escrevendo para um arquivo específico
with open('Trabalho_Pratico/sintatico/entrada_saida/output.txt', 'w') as file:
    file.write(code_to_execute)

print("\nExecutando o código gerado:")
#executando o código no próprio script    
exec(code_to_execute)
