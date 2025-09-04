# MBA Engenharia de Software com IA - FullCycle - Desafio 1

Repositório para armazenar o primeiro desafio do MBA em Engenharia de Software com IA da FullCycle.

## 📋 Sobre o Projeto

Este repositório contém a implementação do primeiro desafio do MBA em Engenharia de Software da FullCycle, onde é possível usar um chat CLI para fazer perguntas a respeito de Teste de Performance em Softwares.
## 🚀 Como Iniciar

### Pré-requisitos

- Python 3.x
- Docker e Docker Compose
- API Key de uma LLM (Large Language Model)

### Instalação e Execução

1. **Instalar dependências**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configurar API Key**
   - Incluir a `API_KEY` da LLM nas variáveis de ambiente ou arquivo de configuração e renomear arquivo .env.example para .env

3. **Iniciar serviços com Docker**
   ```bash
   docker compose up -d
   ```

4. **Executar ingestão de dados**
   ```bash
   python3 src/ingest.py
   ```

5. **Iniciar aplicação de chat**
   ```bash
   python3 src/chat.py
   ```

## 📁 Estrutura do Projeto

```
├── src/
│   ├── ingest.py    # Script para ingestão de dados
│   ├── search.py    # Script para busca de dados
│   └── chat.py      # Aplicação principal de chat
├── requirements.txt # Dependências Python
├── .env.example      # Dependências Python
├── performance.pdf  # Arquivo PDF com dados sobre teste de performance
├── README.md        # Apresentação e instruções do projeto
└── docker-compose.yml # Configuração dos serviços
```

## 🔧 Tecnologias Utilizadas

- Python 3
- Docker
- Docker Compose
- LLM (Large Language Model)
