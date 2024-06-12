# Condicionais.py

Este é um script Python que usa a biblioteca PLY (Python Lex-Yacc) para criar um lexer para uma linguagem de programação simples. A linguagem suporta tipos de dados inteiros, flutuantes e de string, instruções de impressão e instruções condicionais (if-else).

## Requisitos

- Python 3.x
- Biblioteca PLY (Python Lex-Yacc)

Você pode instalar o PLY usando o pip:

```bash
pip install ply
```

## Como executar

Como este é um script Python, não é necessário compilar. Você pode executar o script diretamente usando o interpretador Python.

```bash
python condicionais.py
```	

## Execução

O script lê uma string de entrada que contém o código na linguagem de programação que criei e imprime os tokens reconhecidos. Os tokens são também gravados em um arquivo chamado '[method].txt', onde method representa a pasta que foi chamada.

Por exemplo, a entrada:

```python	
int a = 5
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
```
produzirá a seguinte saída:

```bash
LexToken(INT,'int',1,0)
LexToken(ID,'a',1,4)
LexToken(EQUALS,'=',1,6)
LexToken(NUMBER,5,1,8)
LexToken(NEWLINE,'\n',1,9)

LexToken(FLOAT,'float',2,22)
LexToken(ID,'b',2,28)
LexToken(EQUALS,'=',2,30)
LexToken(FNUMBER,-5.1,2,32)
LexToken(NEWLINE,'\n',2,36)

LexToken(INT,'int',3,49)
LexToken(ID,'c',3,53)
LexToken(EQUALS,'=',3,55)
LexToken(NUMBER,6,3,57)
LexToken(NEWLINE,'\n',3,58)
.
.
.
```


