# Gerador de Chaves de NF-e e Arquivos XML

Este script gera uma quantidade especificada de chaves de Nota Fiscal Eletrônica (NF-e) e cria arquivos XML correspondentes, salvando-os em pastas organizadas.

## Como Executar o Script

### Pré-requisitos

- Python 3 instalado

### Passo a Passo

1. **Clone o repositório ou baixe o script**

   Certifique-se de ter o script `gerar_nfe.py` disponível em seu ambiente local.

2. **Execute o script**

   Para executar o script e especificar a quantidade de chaves desejadas, use a linha de comando conforme o exemplo abaixo:

   ```sh
   python gerar_nfe.py 20

   Neste exemplo, o número 20 é a quantidade de chaves que você deseja gerar. Você pode substituir 20 por qualquer outro número conforme necessário.
O que o Script Faz

    Utiliza argparse para permitir que o usuário especifique a quantidade de chaves a serem geradas.
    Gera a quantidade de chaves especificada.
    Cria uma pasta chamada chaves e salva um arquivo chaves_nfe.txt com as chaves geradas nessa pasta.
    Cria uma pasta chamada nfe e salva um arquivo XML para cada chave gerada nessa pasta.

Desta forma, você pode facilmente gerar o número desejado de chaves e os arquivos XML correspondentes diretamente da linha de comando, organizando-os em suas respectivas pastas.
Estrutura do Projeto

Após a execução do script, a estrutura de diretórios do projeto será a seguinte:

.
├── gerar_nfe.py
├── chaves
│   └── chaves_nfe.txt
└── nfe
    ├── NFe35190712345678000190550010000000011234567891.xml
    ├── NFe35190712345678000190550010000000021234567892.xml
    ├── NFe35190712345678000190550010000000031234567893.xml
    └── ... (outros arquivos XML)

Exemplo de Uso

Para gerar 50 chaves e os arquivos XML correspondentes, execute:

python gerar_nfe.py 50

Isso criará as pastas chaves e nfe (se ainda não existirem) e salvará as chaves e arquivos XML nelas.
