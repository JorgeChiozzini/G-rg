# G-rg
# Assistente Inteligente de Saúde Mental

Este é um aplicativo web para ajudar os usuários a monitorar e melhorar seu bem-estar emocional utilizando o Hugging Face e Flask.

## Funcionalidades

- Registrar sentimentos diários e analisar emoções em texto
- Armazenar entradas de sentimentos no banco de dados
- Exibir histórico de entradas emocionais

## Tecnologias Utilizadas

- Python
- Flask
- Hugging Face Transformers
- SQLite
- HTML/CSS/JavaScript
- Bootstrap
- GitHub Pages

## Como Executar Localmente

1. Clone o repositório
    ```sh
    git clone <URL-do-repositório>
    cd <nome-do-repositório>
    ```

2. Crie e ative um ambiente virtual (opcional, mas recomendado)
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Inicialize o banco de dados:
    - Execute o script de inicialização:
    ```sh
    python -c 'from database import init_db; init_db()'
    ```

5. Execute o aplicativo:
    ```sh
    python app.py
    ```

6. Acesse o aplicativo em `http://127.0.0.1:5000/` no seu navegador.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
