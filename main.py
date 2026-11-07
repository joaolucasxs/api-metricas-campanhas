from fastapi import FastAPI

app = FastAPI(title="API de métricas de campanhas")

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