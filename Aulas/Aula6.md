# Ferramentas para Construção de Compiladores

## Gerador de Analisadores Sintáticos

### Declarações
- Existem duas seções na parte de declarações de um programa YACC, onde ambas são opcionais.

#### Primeira Seção
- Inclui declarações C comuns entre `%{` e `%}`.
- Pode conter declarações de variáveis temporárias ou procedimentos usados nas seções subsequentes.
- Exemplo: `#include <ctype.h>`.

```c
%{
#include <stdio.h>
#include <ctype.h>
%}
```

### Declaração de Tokens

- Tokens são definidos usando `%token`.
- Exemplo: `%token DIGITO`.

### Regras de Tradução

- As regras de tradução são especificadas após o primeiro %%.
- Cada regra consiste em uma produção da gramática e uma ação semântica associada.

#### Forma das Produções

```c

<head> : <body>1 { <ação semântica>1 } |
<body>2 { <ação semântica>2 } |
...
<body>n { <ação semântica>n };

```
- Cadeias de letras e dígitos sem aspas, não declaradas, são consideradas como não-terminais.
- Lados direitos alternativos podem ser separados por uma barra vertical.
- Um ponto-e-vírgula vem após cada lado esquerdo com suas alternativas e suas ações semânticas.
- Um único caractere entre apóstrofos (’c’) é considerado o símbolo terminal c.
- head é considerado o símbolo inicial.
- Uma ação semântica do YACC é uma sequência de instruções C.

#### Referências em Ações Semânticas

- `$$` refere-se ao valor do atributo associado ao símbolo não-terminal head.
- `$i` refere-se ao valor do atributo associado ao i-ésimo símbolo da gramática (terminal ou não-terminal) de body.
- A ação semântica é efetuada sempre que reduzimos pela produção associada.

##### Exemplo de Produção

Para a produção `E → E + T | T`:

```
exp : exp '+' termo { $$ = $1 + $3; } |
      termo { $$ = $1; };
```

## Rotinas de Suporte em C

- A terceira parte de uma especificação YACC consiste em rotinas de suporte em C.
- Um analisador léxico com o nome yylex() precisa ser fornecido.
- Outros procedimentos, como rotinas de recuperação de erros, podem ser acrescentadas.
- O analisador léxico yylex() produz tokens consistindo em um nome de token e seu valor de atributo associado.
- Se um nome de token como DIGIT for retornado, ele deve ser declarado na primeira seção da especificação YACC.
- O valor do atributo associado a um token é passado ao analisador sintático por meio de uma variável chamada yylval definida pelo YACC.

## Precedência e Associatividade
- Pode-se atribuir precedências e associatividades aos símbolos terminais.
- A declaração %left '+' '-' faz com que + e - tenham a mesma precedência e sejam associativos à esquerda.
- A declaração %right '^' define um operador como associativo à direita.
- É possível forçar um operador a ser um operador binário não associativo, escrevendo %nonassoc '<'.

### Precedências de Tokens

- Os tokens recebem precedências na ordem em que aparecem na parte das declarações, a mais baixa primeiro. Os tokens na mesma declaração têm a mesma precedência.
- Quando o símbolo terminal não possui a precedência apropriada a uma produção, é possível forçar a precedência da seguinte forma: %prec <terminal>.

## Exemplo da Calculadora
### Seção de Declaração

```c

%{
#include<stdio.h>
#define YYSTYPE double
%}
%token DIGITO
%left '+'
%left '*'
%right UMINUS

lines : lines exp '\n' { printf("%f \n", $2); }
      | lines '\n'
      | /* vazio */
;
exp : exp '+' exp { $$ = $1 + $3; }
    | exp '-' exp { $$ = $1 - $3; }
    | exp '*' exp { $$ = $1 * $3; }
    | '(' exp ')' { $$ = $2; }
    | '-' exp %prec UMINUS { $$ = - $2; }
    | DIGITO
;

%{
#include<stdio.h>
#include<stdlib.h>
#include "calculadora.tab.h"
%}
%%
[-+]?[0-9]+("."[0-9]*)?([eE]"−"?[0-9]*)? {
    yylval.pont->val = atof(yytext);
    return DIGITO;
}
"+" | "-" | "*" | "/" { return *yytext; }
[ ] { /* pula espaços */ }

```