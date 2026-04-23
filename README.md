# CRM Automation API

API REST desenvolvida para automatizar a gestão de leads comerciais, permitindo cadastro, classificação automática de prioridade, atualização de status no funil de vendas e geração de métricas operacionais em tempo real.

Este projeto foi construído com foco em automação comercial, organização de pipeline de vendas e arquitetura backend escalável, simulando um serviço real utilizado por equipes comerciais e operações de CRM.

---

## Visão Geral

A aplicação recebe leads comerciais via API, processa regras de priorização automaticamente e permite o acompanhamento do avanço desses leads ao longo do funil comercial.

Além disso, disponibiliza endpoints para consulta operacional e métricas estratégicas, facilitando a análise da performance do pipeline.

Este projeto demonstra na prática:

* construção de APIs REST profissionais
* modelagem de dados com banco relacional
* documentação automática com Swagger
* deploy em nuvem
* integração entre backend e banco PostgreSQL
* lógica de automação para priorização comercial

---

## Arquitetura da Solução

A arquitetura segue uma estrutura backend simples e escalável:

Cliente → API Flask → Regras de Negócio → PostgreSQL → Métricas e Monitoramento

### Fluxo operacional:

1. O cliente envia dados do lead para a API
2. A aplicação processa regras de prioridade automaticamente
3. Os dados são persistidos no banco PostgreSQL
4. Os endpoints retornam dados consolidados e métricas do funil

---

## Stack Tecnológica

### Backend

* Python
* Flask
* Flask SQLAlchemy

### Banco de Dados

* PostgreSQL

### Documentação

* Swagger / Flasgger

### Deploy

* Gunicorn
* Render

### Versionamento

* Git
* GitHub

---

## Funcionalidades

### 1. Cadastro de Leads

Permite registrar novos leads com os seguintes campos:

* nome
* email
* empresa
* interesse

No momento do cadastro, a API executa uma lógica automática de priorização:

* Leads com interesse relacionado a IA recebem prioridade **high**
* Demais leads recebem prioridade **medium**

---

### 2. Gestão de Status no Funil

Permite atualizar o estágio do lead no pipeline comercial.

Status disponíveis:

* `new`
* `contacted`
* `qualified`
* `closed`

Essa lógica simula o avanço real de um lead dentro de um CRM comercial.

---

### 3. Métricas Operacionais

O endpoint de métricas retorna dados consolidados do pipeline:

* total de leads cadastrados
* leads novos
* leads contactados
* leads qualificados
* leads fechados
* leads prioritários

Isso fornece visão operacional e comercial da base.

---

### 4. Health Check

Endpoint para verificação da saúde da aplicação, útil para monitoramento e validação do deploy.

---

## Endpoints Disponíveis

---

### Health Check

**GET** `/health`

Verifica se a API está ativa.

**Resposta:**

```json
{
  "status": "ok"
}
```

---

### Criar Lead

**POST** `/leads`

Cria um novo lead na base.

**Body:**

```json
{
  "name": "João Silva",
  "email": "joao@email.com",
  "company": "Empresa X",
  "interest": "Automação com IA"
}
```

**Resposta:**

```json
{
  "message": "Lead criado com sucesso",
  "lead_id": 1
}
```

---

### Listar Leads

**GET** `/leads`

Retorna todos os leads cadastrados.

---

### Atualizar Status

**PUT** `/leads/<id>/status`

Atualiza o status do lead no funil.

**Body:**

```json
{
  "status": "qualified"
}
```

---

### Métricas do Funil

**GET** `/metrics`

Retorna métricas consolidadas do pipeline.

**Resposta:**

```json
{
  "total_leads": 12,
  "new": 4,
  "contacted": 3,
  "qualified": 3,
  "closed": 2,
  "high_priority": 5
}
```

---

## Documentação Online

### API Base URL

https://crm-automation-api.onrender.com

### Swagger

https://crm-automation-api.onrender.com/apidocs

A documentação interativa permite testar todos os endpoints diretamente pelo navegador.

---

## Estrutura do Projeto

```bash
crm-automation-api/
│── app.py
│── config.py
│── requirements.txt
│── README.md
```

### Descrição dos arquivos:

* `app.py` → inicialização da aplicação e rotas da API
* `config.py` → configuração da conexão com banco e ambiente
* `requirements.txt` → dependências do projeto
* `README.md` → documentação do projeto

---

## Regras de Negócio Implementadas

### Priorização automática de leads

Se o campo `interest` contiver referência a IA:

```python
priority = "high"
```

Caso contrário:

```python
priority = "medium"
```

Essa regra simula um processo de qualificação automatizada dentro de operações comerciais.

---

## Objetivos Técnicos do Projeto

Este projeto foi desenvolvido para demonstrar competências em:

* desenvolvimento backend com Python
* criação de APIs REST
* integração com PostgreSQL
* documentação de APIs com Swagger
* deploy em ambiente cloud
* modelagem de entidades comerciais
* automação de regras de negócio
* organização de arquitetura backend

---

## Melhorias Futuras

O projeto foi estruturado para futuras evoluções como:

### Segurança

* autenticação JWT
* controle de acesso por usuário

### Escalabilidade

* separação em camadas (controllers, services, repositories)
* uso de migrations com Flask-Migrate

### Inteligência Comercial

* lead scoring avançado
* automação de follow-up
* integração com CRMs externos

### Observabilidade

* logs estruturados
* monitoramento de erros
* métricas de performance

### Frontend

* dashboard administrativo em React
* gráficos em tempo real
* visão visual do pipeline

---

## Resultado do Projeto

Ao final, a solução entrega:

* API pública documentada
* banco de dados em nuvem
* regras automáticas de priorização
* métricas comerciais consolidadas
* deploy funcional em produção

Isso representa a construção de um backend real orientado a automação comercial.

---

## Autor

Desenvolvido por **Kaue Aguiar**

Projeto focado em backend, automação comercial e soluções inteligentes com APIs escaláveis.

versionamento da API
