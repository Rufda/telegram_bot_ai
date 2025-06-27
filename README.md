# Telegram AI Bot

Questo progetto contiene un semplice bot Telegram basato su [aiogram](https://github.com/aiogram/aiogram) e [OpenAI GPT-3.5-turbo](https://platform.openai.com/docs/guides/chat). Il bot risponde a ogni messaggio ricevuto generando il testo tramite OpenAI.

## Requisiti
- Python 3.11 o superiore
- Un account Telegram con un bot token
- Una chiave API di OpenAI

## Configurazione locale
1. Clona questo repository e installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```
2. Esporta le variabili d'ambiente:
   ```bash
   export TELEGRAM_BOT_TOKEN=il_tuo_token
   export OPENAI_API_KEY=la_tua_chiave
   ```
3. Avvia il bot:
   ```bash
   python main.py
   ```

## Deploy su Render
1. Crea un nuovo servizio di tipo **Web Service** su [Render](https://dashboard.render.com/). Seleziona questo repository GitHub e usa il file `render.yaml` incluso.
2. Durante la configurazione, aggiungi le variabili d'ambiente nella sezione **Environment**:
   - `TELEGRAM_BOT_TOKEN`: il token del bot Telegram
   - `OPENAI_API_KEY`: la tua chiave API OpenAI
3. Completa la creazione del servizio. Render installerà automaticamente le dipendenze e avvierà il bot con `python main.py`.

Il bot sarà quindi online 24/7 sul piano gratuito di Render.

## Sicurezza
Le chiavi API **non** sono presenti nel codice sorgente e devono essere fornite solo tramite variabili d'ambiente. Assicurati di non condividere mai i tuoi token pubblicamente.
