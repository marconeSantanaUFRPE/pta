# Protocolo de Transferência de Arquivos - PTA

Servidor para protocolo de transferência de arquivo feito em python para a disciplina de SISTEMAS DE INFORMAÇÃO NA INTERNET do curso de sistemas de informação da UFRPE


Requisito:
```
Python 3 instalado na máquina
```
Para iniciar Servidor:
```
Execute o arquivo pta-server.py
```


Módulos Utilizados no pta-server.py:
  ```
   1. Socket - Módulo que oferece uma interface para a API de sockets. 
   Os métodos utilizados foram:
    -socket() - método para instanciar um socket
    -bind() - associa o socket servidor a um endereço
    -listen() -  método para ouvir conexão
    -accept() -  método para aceitar a conexão de cliente
    -recv() - método para leitura de bytes. lê os bytes retornando em uma string
    -close() -  método para fechar o socket
    -send() - método para envio de bytes
  
    2. OS - Este módulo fornece uma maneira simples de usar funcionalidades que são dependentes do sistema operacional.
    Os métodos utilizados foram:
    -path() - método para encontrar caminhos dos arquivos necessários (users.txt) e para acessar a pasta files e obter informações sobre os arquivos
    -walk() - O método que gera os nomes dos arquivos em uma árvore de diretórios 
```
