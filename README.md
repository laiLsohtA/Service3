# Serviço 3 - Analisador de Tarefas

## 📊 Função
Este serviço é responsável por analisar as tarefas de um usuário autenticado e retornar estatísticas.

## 🔐 Autenticação
Utiliza JWT no header:
Authorization: Bearer <token>

## 📌 Endpoint

GET /stats

## 📥 Resposta

{
  "usuarioId": 1,
  "total": 10,
  "concluidas": 6,
  "pendentes": 4
}

## 🛠 Tecnologias
- Python
- FastAPI
- SQLAlchemy

## Banco DATABASE
Coloque o link de um banco de dados MySQL para o DATABASE_URL