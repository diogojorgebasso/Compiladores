import ply.yacc as yacc
import sys
sys.path.insert(0, 'D:/code/Compiladores/Trabalho_Pratico/lexico')
from condicionais import tokens

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
                 | print_statement
                 | conditional_statement'''
    p[0] = p[1]

def p_declaration(p):
    '''declaration : type ID EQUALS expression NEWLINE'''
    p[0] = f"{p[2]} = {p[4]}\n"

def p_conditional_statement(p):
    '''conditional_statement : IF LPAREN condition RPAREN LBRACKET NEWLINE print_statement RBRACKET NEWLINE
                             | IF LPAREN condition RPAREN LBRACKET NEWLINE print_statement RBRACKET ELSE LBRACKET NEWLINE print_statement RBRACKET NEWLINE'''
    
    if len(p) == 10:
        p[0] = f"if {p[3]}:\n{indent(p[7])}"
    else:
        p[0] = f"if {p[3]}:\n{indent(p[7])}else:\n{indent(p[12])}"

def p_print_statement(p):
    '''print_statement : PRINT LPAREN ID RPAREN NEWLINE
                       | PRINT LPAREN STRING RPAREN NEWLINE'''
    if p[3].startswith(("'", '"')):  # If it's a string literal
        p[0] = f'print({p[3]})\n'  # Keep the quotes
    else:  # It's an identifier
        p[0] = f'print({p[3]})\n'  # No need to add quotes, corrected logic
    
def p_condition(p):
    '''condition : expression comparator expression
                 | expression comparator expression AND condition
                 | expression comparator expression OR condition'''
    if len(p) == 4:
        p[0] = f"{p[1]} {p[2]} {p[3]}"
    else:
        p[0] = f"{p[1]} {p[2]} {p[3]} {p[4]} {p[5]}"

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
    p[0] = str(p[1])

def p_error(p):
    if p:
        print("Sintaxe erro do valor '%s' na linha %d" % (p.value, p.lineno))
    else:
        print("Erro de sintaxe no final do arquivo!")

def indent(code_block, level=1):
    indentation = '    '  # 4 spaces
    if isinstance(code_block, list):
        code_block = "\n".join(code_block)
    indented_code = ''.join(f"{indentation*level}{line}\n" for line in code_block.splitlines())
    return indented_code

parser = yacc.yacc()

data = '''int a = 5
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
'''
result = parser.parse(data)
code_to_execute = ''.join(result)

# escrevendo para um arquivo específico
with open('Trabalho_Pratico/sintatico/condicionais/output.txt', 'w') as file:
    file.write(code_to_execute)

print("Compilado com sucesso!")
#executando o código no próprio script    
exec(code_to_execute)
