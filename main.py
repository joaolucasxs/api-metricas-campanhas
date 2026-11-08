from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="API de métricas de campanhas")

class Campanha(BaseModel):
    nome: str
    data: str
    gasto: float
    impressoes: int
    cliques: int
    conversoes: int
    receita: float

campanhas: list[Campanha] = []

@app.get("/")
def raiz():
    return {"status": "ok", "mensagem": "API no ar"}

@app.get("/metricas/exemplo")
def exemplo():
    gasto, cliques, conversoes, receita = 1000.0, 400, 20, 7000.0
    return {
        "cpa": round(gasto / conversoes, 2),
        "roas": round(receita / gasto, 2),
        "taxa_conversao": round(conversoes / cliques * 100, 2),
    }

@app.get("/metricas/calcular")
def calcular(gasto: float, impressoes: int, cliques: int, conversoes: int, receita: float):
    if impressoes == 0 or cliques == 0 or conversoes == 0 or gasto == 0:
        return {"erro": "impressoes, cliques, conversoes e gasto precisam ser maiores que zero"}
    return {
        "ctr": round(cliques / impressoes * 100, 2),
        "cpc": round(gasto / cliques, 2),
        "cpa": round(gasto / conversoes, 2),
        "roas": round(receita / gasto, 2),
        "taxa_conversao": round(conversoes / cliques * 100, 2),
    }


@app.post("/campanhas")
def registrar_campanha(campanha: Campanha):
    campanhas.append(campanha)
    return {"mensagem": "campanha registrada", "total": len(campanhas)}

@app.get("/campanhas")
def listar_campanhas():
    return campanhas