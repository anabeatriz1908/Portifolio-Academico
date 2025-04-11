
# 🔗 API de Gestão Acadêmica 

Este projeto consiste em uma API RESTful desenvolvida com **Flask**, com foco na implementação de um CRUD completo para três entidades: **Aluno**, **Professor** e **Curso**. O projeto foi desenvolvido em grupo como parte de um trabalho acadêmico, utilizando boas práticas como a arquitetura de **blueprints**, separação por camadas e uso de arquivos de configuração.

---

## 🔧 Tecnologias Utilizadas

- Python 3.11+
- Flask
- Flask SQLAlchemy
- Flask Migrate
- Blueprints
- Postman (para testes)

---

## 📁 Estrutura do Projeto

```
Entrega 02/
│
├── app.py                  # Arquivo principal para rodar a aplicação
├── config.py               # Configurações de ambiente
├── requirements.txt        # Dependências do projeto
│
└── main/
    ├── Aluno/              # Módulo da entidade Aluno
    ├── Professor/          # Módulo da entidade Professor
    └── Curso/              # Módulo da entidade Curso
```

---

## ▶️ Como Rodar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. **Crie um ambiente virtual:**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Instale as dependências:**

```bash
pip install -r requirements.txt
```

4. **Rode as migrações (se necessário):**

```bash
flask db init
flask db migrate
flask db upgrade
```

5. **Execute a aplicação:**

```bash
python app.py
```

A API estará disponível em: `http://localhost:5036`

---

## 📌 Funcionalidades

Cada entidade possui os seguintes endpoints:

- **GET** `/entidade` – Lista todos os registros
- **GET** `/entidade/<id>` – Busca um registro por ID
- **POST** `/entidade` – Cria um novo registro
- **PUT** `/entidade/<id>` – Atualiza um registro
- **DELETE** `/entidade/<id>` – Remove um registro
- **DELETE** `/entidade` - Reseta todos os registros

*(Substitua `entidade` por `alunos`, `professores` ou `turmas`)*

---

## 🤝 Colaboradores

Este projeto foi desenvolvido por em grupo como parte de um projeto da matéria de Desenvolvimento de API na Faculdade Impacta

---

## 📬 Contato

Caso queira entrar em contato para sugestões ou dúvidas, fique à vontade para me procurar por aqui mesmo ou via [LinkedIn](https://www.linkedin.com/in/ana-beatriz-silva-santos/) ou via E-mail ana1908beatrizsantos@gmail.com

