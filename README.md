Como Usar o Projeto
1. Instalar Dependências:
   * No diretório do projeto, execute:
        ```bash
        pip install -r requirements.txt
        ```
2. Pegar API_KEY:
   * No site https://next.nexusmods.com/settings/api-keys logado, basta copiar a Personal API Key localizada ao final do site
3. Configure a variável de ambiente:
    * Via PyCharm no caminho: "Run > Edit Configurations > Environment Variables" adicione a variável API_KEY="valor pego no site"
4. Executar o Projeto:
    * Para rodar o projeto, basta executar o main.py:
        ```bash
        python main.py
        ```