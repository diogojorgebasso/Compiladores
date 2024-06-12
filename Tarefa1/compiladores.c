#include <stdio.h>
#include <string.h>

#define TAMANHO 100

/* O automato escolhido foi o primeiro*/
/* Copyright Diogo Basso*/

void reconhece(char cadeia[TAMANHO])
{
  int tam, i, estado = 0;

  tam = strlen(cadeia);

  for (i = 0; i < tam; i++)
  {
    printf("%d\n", estado);
    printf("%d\n", i);
    switch (cadeia[i])
    {
    case 'X':
      if (estado == 0)
      {
        estado = 9;
        break;
      }
      else
      {
        if (estado == 2)
        {
          estado = 6;
          break;
        }
        else
        {
          estado = 99;
          break;
        }
      }
    case 'V':
      if (estado == 0)
      {
        estado = 7;
        break;
      }
      else
      {
        if (estado == 2)
        {
          estado = 5;
          break;
        }
        else
        {
          estado = 99;
          break;
        }
      }
    case 'I':
      if (estado == 0)
      {
        estado = 2;
        break;
      }
      else
      {
        if (estado == 2)
        {
          estado = 3;
          break;
        }
        else
        {
          if (estado == 3)
          {
            estado = 4;
            break;
          }
          else
          {
            if (estado == 7)
            {
              estado = 8;
              break;
            }
            else
            {
              if (estado == 8)
              {
                estado = 3;
                break;
              }
              else
              {
                estado = 99;
                break;
              }
            }
          }
        }
      }
    default:
      estado = 99;
      break;
    }
  }
  if ((estado == 99) || (estado == 0))
    printf("\n Numero romano nao reconhecido \n");
  else
  {
    printf("\n Numero romano reconhecido \n");
  }
}

int main(int argc, char **argv)
{
  char cadeia[TAMANHO];

  while (1)
  {
    printf("\n Entrada = ");
    scanf("%s", cadeia);

    if (strcmp(cadeia, "s") == 0)
      break;

    reconhece(cadeia);
    getchar();
  }
  printf("\n Terminando ... \n");
  return 0;
}
