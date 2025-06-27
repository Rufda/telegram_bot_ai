# telegram-ai-bot

Bot Telegram basato su GPT che risponde ai messaggi degli utenti.

## Configurazione

1. Clona questo repository e assicurati di avere Python 3.10 o superiore.
2. Installa le dipendenze:
   ```bash
   pip install -r requirements.txt
   ```
3. Esporta le variabili d'ambiente con i tuoi token:
   ```bash
   export TELEGRAM_BOT_TOKEN=...  # il token del tuo bot Telegram
   export OPENAI_API_KEY=...      # la tua chiave OpenAI
   ```
4. Avvia il bot localmente con:
   ```bash
   python main.py
   ```

## Deploy su Render

1. Crea un nuovo repository GitHub e carica questi file.
2. Su [Render](https://dashboard.render.com), crea un **Web Service** collegandolo al repository.
3. Durante la configurazione del servizio:
   - Imposta `render.yaml` come file di configurazione.
   - Aggiungi le variabili d'ambiente `TELEGRAM_BOT_TOKEN` e `OPENAI_API_KEY` con i tuoi valori.
4. Completa la procedura di deploy: Render installer\u00e0 automaticamente le dipendenze e avvier\u00e0 il bot.

Una volta avviato, il bot sar\u00e0 online 24/7 e risponder\u00e0 ai messaggi su Telegram.
