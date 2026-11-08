# API de métricas de campanhas

API em FastAPI para registrar e calcular métricas de campanhas de mídia paga (CTR, CPA, ROAS). Projeto de estudo de backend, construído em etapas.

## O que já funciona
- `GET /` — status da API
- `GET /metricas/exemplo` — calcula CPA, ROAS e taxa de conversão a partir de valores fixos
- `GET /metricas/calcular` — recebe gasto, impressões, cliques, conversões e receita pela URL e devolve CTR, CPC, CPA, ROAS e taxa de conversão
- `POST /campanhas` — registra uma campanha (em memória, por enquanto)
- `GET /campanhas` — lista as campanhas registradas
- Documentação automática em `/docs`

## Como rodar
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
```
Abrir http://127.0.0.1:8000/docs

## Próximos passos
- [x] Receber os números por parâmetro em vez de valores fixos
- [x] Registrar campanhas por POST
- [ ] Guardar em banco de dados (SQLite)
- [ ] Calcular métricas a partir das campanhas registradas