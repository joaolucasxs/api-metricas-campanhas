# API de métricas de campanhas

API em FastAPI para registrar e calcular métricas de campanhas de mídia paga (CTR, CPA, ROAS). Projeto de estudo de backend, construído em etapas.

## O que já funciona
- `GET /` — status da API
- `GET /metricas/exemplo` — calcula CPA, ROAS e taxa de conversão a partir de valores fixos
- Documentação automática em `/docs`

## Como rodar
```
pip install fastapi uvicorn
python -m uvicorn main:app --reload
```
Abrir http://127.0.0.1:8000/docs

## Próximos passos
- [ ] Receber os números por parâmetro em vez de valores fixos
- [ ] Registrar campanhas por POST
- [ ] Guardar em banco de dados
