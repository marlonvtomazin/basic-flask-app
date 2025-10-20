# Aplicação simples utilizando Flask

### 🛠️ Tecnologias Utilizadas

* **Backend -> Python 3:** Linguagem principal.
* **Framework -> Flask:** Roteamento e estrutura de aplicação web.
* **Templates -> Jinja2:** Renderização dinâmica do HTML.
* **Frontend -> cru.js:** Manipulação de eventos de formulário (POST/PUT/DELETE) via AJAX para atualização do DOM (lista de clientes).
* **Estilo -> Bootstrap:** Componentes e estilização responsiva.
* **Banco de dados -> SQLite:** Banco de dados leve e baseado em arquivo para persistência dos dados de desenvolvimento e produção inicial.
* **ORM -> peewee:** Mapeamento Objeto-Relacional (ORM) para definição dos modelos e manipulação do banco de dados (CRUD).

Instalação e execução

Crie um ambiente virtual
```
python -m venv venv_flask
```

Entre no ambiente virtual
```
.\venv_flask\Scripts\activate
```

Instale as dependencias
```
pip install -r requirements.txt
```

Execute o arquivo principal
```
py .\main.py
```