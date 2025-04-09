# 🤖 Mini-Projeto de Automação Robótica com Python (RPA)

Este projeto foi desenvolvido como parte da AP1 (Avaliação Parcial 01) da disciplina de Desenvolvimento com Automação Robótica de Processos, com o objetivo de aplicar conceitos de automação robótica utilizando Python. O assistente virtual automatizado criado executa tarefas como abrir programas, fazer pesquisas, capturar telas e navegar por imagens, tudo de forma automática.

---

## 📋 Descrição do Projeto

O script executa ações com base em um arquivo CSV que contém uma lista de tarefas organizadas por tipo e dados associados. Ele utiliza a biblioteca `PyAutoGUI` para automação do teclado e mouse, `pandas` para leitura de arquivos e `openpyxl` para gerar relatórios no Excel.

### 🗂 Exemplo de Entrada (tarefas.csv)

```csv
Tarefa,Tipo,Dado
Abrir,enter,Calculadora
Pesquisar,chrome,Guerra dos Canudos
Capturar,none,none
Mostrar galeria,enter,Fotos
Desconhecida,enter,Excel
```

---

## ⚙️ Funcionalidades

- **Leitura de tarefas** a partir de um arquivo `.csv`.
- **Execução automática** com base no tipo de tarefa:
  - `Abrir`: abre programas no menu iniciar.
  - `Pesquisar`: abre navegador e faz uma pesquisa.
  - `Capturar`: captura uma região da tela selecionada pelo usuário.
  - `Mostrar galeria`: abre aplicativo de fotos e navega pelas imagens.
- **Geração de relatório** com:
  - Nome da tarefa
  - Status de execução (sucesso ou falha)
  - Tempo de execução (em segundos)

---

## 🧠 Tecnologias e Bibliotecas Utilizadas

- `pyautogui` – automação de teclado e mouse
- `pandas` – manipulação de dados
- `openpyxl` – geração de planilhas Excel
- `pygetwindow` – verificação de janelas abertas
- `datetime`, `time`, `os` – recursos auxiliares

---

## 📦 Estrutura do Projeto

```
mini-projeto-rpa/
├── aut.py                  # Script principal
├── tarefas.csv             # Lista de tarefas para automação
├── tarefas-realizadas.xlsx # Gerado automaticamente
└── README.md               # Este documento
```

---

## 📝 Como Executar

1. Instale as dependências:
   ```bash
   pip install pyautogui pandas openpyxl pygetwindow
   ```

2. Execute o script:
   ```bash
   python automacao.py
   ```

3. Interaja com os alertas e seleções de tela para concluir as automações.

---

## 🧾 Relatório Gerado

Ao final da execução, o programa gera automaticamente um arquivo Excel com um resumo das tarefas realizadas, indicando:
- Tarefa
- Status de execução
- Tempo estimado

---

## 👥 Projeto em Dupla

Este projeto foi desenvolvido em dupla para fins acadêmicos como parte da AP1, utilizando conhecimentos práticos de automação, manipulação de arquivos e estruturas condicionais.

## 📝 Licença

Este projeto é apenas para fins educacionais.
