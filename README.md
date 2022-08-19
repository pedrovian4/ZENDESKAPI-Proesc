# tickets_API
Consumo de API para preencher campo da Entidade Eternal_id do Zendesk


### updateDB
 - Realiza filtragem de dados nulos na API até a paginação 24 por padrão
 - Filtra entidades ID nulas
 - Update no banco de dados
#### Como executar
- para executar cada modulo é preciso está dentro do módulo respectivo
- Instalar python3
- Instalar pip 
- Instalar python3 virtualenv
     ```
        python3 -m venv venv
        source venv/bin/activate 
        pip install -r requirements.txt
    ```
- executar comandos as mos arquivos main com
    ```
    python3 main.py
    ```
