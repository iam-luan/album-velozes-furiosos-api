# 🚗 Album Velozes & Furiosos API

API REST desenvolvida com **FastAPI** para fornecer os dados e imagens das figurinhas utilizadas no projeto **Velozes & Furiosos - Álbum Oficial Colecionador**.

---

## 🎯 Objetivo

Esta API é responsável por disponibilizar as informações e imagens das figurinhas consumidas pelo frontend, permitindo uma integração simples e eficiente através de requisições HTTP.

---

## 🚀 Funcionalidades

- 📋 Listagem de todas as figurinhas.
- 🔍 Consulta de figurinhas por ID.
- 🖼️ Disponibilização das imagens das figurinhas.
- 🌐 Configuração de CORS para integração com o frontend.
- 📖 Documentação automática da API utilizando FastAPI.

---

## 🛠️ Tecnologias Utilizadas

- Python
- FastAPI
- Uvicorn

---

## 📂 Estrutura do Projeto

```text
album-velozes-furiosos-api/
│
├── figurinhas/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🌐 API Online

A API está disponível em:

**https://album-velozes-furiosos-api.onrender.com**

### 📖 Documentação (Swagger)

https://album-velozes-furiosos-api.onrender.com/docs

### 📚 Documentação (ReDoc)

https://album-velozes-furiosos-api.onrender.com/redoc

---

## ▶️ Como Executar Localmente

### 1. Clone o repositório

```bash
git clone https://github.com/iam-luan/album-velozes-furiosos-api.git
```

### 2. Acesse a pasta do projeto

```bash
cd album-velozes-furiosos-api
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

**Windows**

```bash
venv\Scripts\activate
```

**Linux/macOS**

```bash
source venv/bin/activate
```

### 5. Instale as dependências

```bash
pip install -r requirements.txt
```

### 6. Execute a aplicação

```bash
uvicorn main:app --reload
```

A API ficará disponível em:

```
http://localhost:8000
```

---

## 🎨 Frontend

O frontend deste projeto está disponível em:

**GitHub:**  
https://github.com/iam-luan/Album-Velozes-e-furiosos

---

##  Desenvolvedor

Desenvolvido por **Luan Alcantara**.
