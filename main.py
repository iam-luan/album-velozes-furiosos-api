from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import glob

# Cria a instância principal da aplicação FastAPI
app = FastAPI()

# Configuração do Middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Definição dos caminhos absolutos para encontrar as imagens de forma segura
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista com as 40 figurinhas mapeadas de acordo com as páginas do álbum HTML
figurinhas = [
    # PAGINA 1: A FAMÍLIA (Ativos)
    {"id": 1, "nome": "Dominic Toretto", "categoria": "Pilotos", "imagem_url": "/figurinhas/1/imagem"},
    {"id": 2, "nome": "Brian O'Conner", "categoria": "Pilotos", "imagem_url": "/figurinhas/2/imagem"},
    {"id": 3, "nome": "Mia Toretto", "categoria": "Pilotos", "imagem_url": "/figurinhas/3/imagem"},
    {"id": 4, "nome": "Letty Ortiz", "categoria": "Pilotos", "imagem_url": "/figurinhas/4/imagem"},
    {"id": 5, "nome": "Roman Pearce", "categoria": "Pilotos", "imagem_url": "/figurinhas/5/imagem"},

    # PAGINA 2: PARCEIROS (Indisponíveis)
    # {"id": 6, "nome": "Luke Hobbs", "categoria": "Pilotos", "imagem_url": "/figurinhas/6/imagem"},
    # {"id": 7, "nome": "Tej Parker", "categoria": "Pilotos", "imagem_url": "/figurinhas/7/imagem"},
    # {"id": 8, "nome": "Han Lue", "categoria": "Pilotos", "imagem_url": "/figurinhas/8/imagem"},
    # {"id": 9, "nome": "Gisele Yashar", "categoria": "Pilotos", "imagem_url": "/figurinhas/9/imagem"},
    # {"id": 10, "nome": "Deckard Shaw", "categoria": "Pilotos", "imagem_url": "/figurinhas/10/imagem"},

    # PAGINA 3: RIVAIS (Indisponíveis)
    # {"id": 11, "nome": "Cipher", "categoria": "Pilotos", "imagem_url": "/figurinhas/11/imagem"},
    # {"id": 12, "nome": "Hernan Reyes", "categoria": "Pilotos", "imagem_url": "/figurinhas/12/imagem"},
    # {"id": 13, "nome": "Owen Shaw", "categoria": "Pilotos", "imagem_url": "/figurinhas/13/imagem"},
    # {"id": 14, "nome": "Mose Jakande", "categoria": "Pilotos", "imagem_url": "/figurinhas/14/imagem"},
    # {"id": 15, "nome": "Dante Reyes", "categoria": "Pilotos", "imagem_url": "/figurinhas/15/imagem"},

    # PAGINA 4: EQUIPE (Indisponíveis)
    # {"id": 16, "nome": "Ramsey", "categoria": "Pilotos", "imagem_url": "/figurinhas/16/imagem"},
    # {"id": 17, "nome": "Jakob Toretto", "categoria": "Pilotos", "imagem_url": "/figurinhas/17/imagem"},
    # {"id": 18, "nome": "Sean Boswell", "categoria": "Pilotos", "imagem_url": "/figurinhas/18/imagem"},
    # {"id": 19, "nome": "Mr. Nobody", "categoria": "Pilotos", "imagem_url": "/figurinhas/19/imagem"},
    # {"id": 20, "nome": "Elena Neves", "categoria": "Pilotos", "imagem_url": "/figurinhas/20/imagem"},

    # PAGINA 5: MÁQUINAS - PARTE 1 (Ativos)
    {"id": 21, "nome": "Dodge Charger R/T", "categoria": "Carros", "imagem_url": "/figurinhas/21/imagem"},
    {"id": 22, "nome": "Toyota Supra RZ", "categoria": "Carros", "imagem_url": "/figurinhas/22/imagem"},
    {"id": 23, "nome": "Nissan Skyline GT-R", "categoria": "Carros", "imagem_url": "/figurinhas/23/imagem"},
    {"id": 24, "nome": "Mazda RX-7 Veilside", "categoria": "Carros", "imagem_url": "/figurinhas/24/imagem"},
    {"id": 25, "nome": "Mitsubishi Eclipse", "categoria": "Carros", "imagem_url": "/figurinhas/25/imagem"},

    # PAGINA 6: MÁQUINAS - PARTE 2 (Indisponíveis)
    # {"id": 26, "nome": "Honda Civic EJ1", "categoria": "Carros", "imagem_url": "/figurinhas/26/imagem"},
    # {"id": 27, "nome": "Chevrolet Chevelle SS", "categoria": "Carros", "imagem_url": "/figurinhas/27/imagem"},
    # {"id": 28, "nome": "Ford Escort RS1600", "categoria": "Carros", "imagem_url": "/figurinhas/28/imagem"},
    # {"id": 29, "nome": "Lykan Hypersport", "categoria": "Carros", "imagem_url": "/figurinhas/29/imagem"},
    # {"id": 30, "nome": "Sua Máquina Favorita", "categoria": "Carros", "imagem_url": "/figurinhas/30/imagem"},

    # PAGINA 7: DESAFIO EM TÓQUIO (Indisponíveis)
    # {"id": 31, "nome": "Nissan Silvia S15", "categoria": "Carros", "imagem_url": "/figurinhas/31/imagem"},
    # {"id": 32, "nome": "Lancer Evolution IX", "categoria": "Carros", "imagem_url": "/figurinhas/32/imagem"},
    # {"id": 33, "nome": "Nissan 350Z (Z33)", "categoria": "Carros", "imagem_url": "/figurinhas/33/imagem"},
    # {"id": 34, "nome": "Ford Mustang 1967", "categoria": "Carros", "imagem_url": "/figurinhas/34/imagem"},
    # {"id": 35, "nome": "Volkswagen Touran", "categoria": "Carros", "imagem_url": "/figurinhas/35/imagem"},

    # PAGINA 8: GARAGEM ALCÂNTARA - ÚLTIMA PÁGINA (Ativos)
    {"id": 36, "nome": "Volkswagen Jetta GLI", "categoria": "Carros", "imagem_url": "/figurinhas/36/imagem"},
    {"id": 37, "nome": "Porsche 911 GT3", "categoria": "Carros", "imagem_url": "/figurinhas/37/imagem"},
    {"id": 38, "nome": "Dodge Charger Daytona", "categoria": "Carros", "imagem_url": "/figurinhas/38/imagem"},
    # {"id": 39, "nome": "Corvette Grand Sport", "categoria": "Carros", "imagem_url": "/figurinhas/39/imagem"},
    # {"id": 40, "nome": "Sua Próxima Máquina", "categoria": "Carros", "imagem_url": "/figurinhas/40/imagem"}
]

# Endpoint para listar apenas as figurinhas ativas
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas

# Endpoint para servir a imagem correspondente à figurinha com base no ID
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    # Constrói o padrão de busca com base no ID formatado com 2 dígitos seguido por caractere não numérico
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    
    # Busca arquivos no diretório que correspondem ao padrão
    arquivos = glob.glob(padrao)
    
    # Se não encontrar nenhum arquivo correspondente, lança erro HTTP 404
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    
    # Retorna o arquivo correspondente (o primeiro encontrado caso haja duplicidade)
    return FileResponse(arquivos[0])
