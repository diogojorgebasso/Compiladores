# Autômato de Identificação de Número Romano de I para X

Este autômato foi criado em C para identificar números romanos de I (1) para X (10). Ele funciona através da leitura de caracteres de entrada e do uso de um conjunto de estados para determinar se a sequência de caracteres representa um número romano válido.

O autômato possui os seguintes estados:

- **Estado inicial**: O autômato começa neste estado. Se o primeiro caractere for 'I', ele passa para o estado 2. Se for 'V', ele identifica o número como 7. Se for 'X', ele identifica o número como 9.
- **Estado 2**: Se o próximo caractere for 'I', ele passa para o estado 3. Se for 'V', ele identifica o número como 5. Se for 'X', ele identifica o número como 6.
- **Estado 3**: Se o próximo caractere for 'I', ele identifica o número como 4.
- **Estado 7**: Se o próximo caractere for 'I', ele passa para o estado 8.
- **Estado 8**: Se o próximo caractere for 'I', ele identifica o número como 3.

É válido ressltar que todos os estados, além do inicial, são finais, ou seja, ao chegar em um desses estados, o autômato aceita a entrada como um último número romano válido.

Se em qualquer ponto o autômato receber um caractere que não seja 'I', 'V' ou 'X', ele rejeitará a entrada como um número romano inválido, indo para o estado 99.