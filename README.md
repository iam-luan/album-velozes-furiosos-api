# 🚗 Album Velozes e Furiosos API

API REST desenvolvida com FastAPI para fornecer os dados do álbum de figurinhas Velozes e Furiosos.

## 🚀 Tecnologias

- Python 3
- FastAPI
- Uvicorn

## 📋 Funcionalidades

- Listagem das figurinhas
- Consulta de figurinha por ID
- Retorno das imagens das figurinhas
- Configuração de CORS para integração com o frontend

## ▶️ Como executar

Clone o projeto:

```bash
git clone https://github.com/iam-luan/album-velozes-furiosos-api.git
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute:

```bash
uvicorn main:app --reload
```

A API ficará disponível em:

```
http://localhost:8000
```

Documentação automática:

- http://localhost:8000/docs
- http://localhost:8000/redoc

## 🎨 Frontend

O frontend da aplicação está disponível em:

https://github.com/iam-luan/Album-Velozes-e-furiosos-frontend
