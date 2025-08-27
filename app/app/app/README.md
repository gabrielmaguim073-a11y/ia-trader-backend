# IA Trader Backend 🚀

Backend em **FastAPI** para gerar sinais de trading em tempo real.

## Rotas disponíveis
- `GET /` → verifica se o servidor está online
- `WS /ws/signals` → envia sinais (BUY / SELL / HOLD) em tempo real

## Estratégia
A IA usa **RSI (Relative Strength Index)**:
- RSI < 30 → BUY
- RSI > 70 → SELL
- Caso contrário → HOLD

## Deploy no Railway
1. Crie um fork deste repositório
2. No Railway: **New Project → Deploy from GitHub Repo**
3. Selecione o fork
4. Railway vai gerar uma URL pública, ex:
