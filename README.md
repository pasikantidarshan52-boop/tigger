# 🐯 Tigger — your own Gemini-style AI assistant

A full-stack Python app: **Flask** backend (multi-user accounts, saved chat history, streaming replies)
and a **light-blue** responsive web frontend (desktop + phone). Tigger can run on
**Google Gemini**, **Anthropic Claude**, **OpenAI / any OpenAI-compatible server** (Ollama, LM Studio…),
or in **demo mode** with no API key.

## Features
- Sign up / sign in; every user has private chats stored in SQLite
- Streaming answers, Markdown and code blocks with a Copy button
- New / delete chats, history sidebar, automatic chat titles
- Mobile friendly, no build step, no external CDNs
- Docker ready for hosting to many users

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env               # Windows: copy .env.example .env
python run.py
```
Open **http://localhost:8000**, create an account and chat. It starts in *demo mode*.

## Turn on the real AI
Edit `.env`, then restart:
```
TIGGER_PROVIDER=gemini
GEMINI_API_KEY=your-key        # free key: https://aistudio.google.com/apikey
```
Other options: `TIGGER_PROVIDER=anthropic` + `ANTHROPIC_API_KEY`, or `openai` + `OPENAI_API_KEY`
(set `OPENAI_BASE_URL=http://localhost:11434/v1` for a local Ollama server).

## Let many people use it
- **Same network / a server:** `python run.py` listens on all interfaces; share `http://<your-ip>:8000`.
  For the public internet, put it behind HTTPS (Caddy, Nginx, Cloudflare Tunnel…).
- **Docker:** `cp .env.example .env` (add provider + key), then `docker compose up -d --build`.
  User data persists in the `tigger-data` volume.
- **Control sign-ups:** set `TIGGER_ALLOW_SIGNUP=0` and add users yourself:
  ```bash
  python manage.py create-user alice@example.com StrongPass123 Alice
  python manage.py list-users
  ```
All users share your API key and quota, so keep sign-ups closed (or add rate limiting) for public deployments.

## Layout
```
run.py            start the server
manage.py         admin helper (create / list users)
app/main.py       Flask routes: auth, chats, streaming
app/llm.py        AI providers (Gemini / Claude / OpenAI / demo): add your own here
app/auth.py       password hashing + JWT login tokens
app/db.py         SQLite schema
app/config.py     settings from .env, plus Tigger's system prompt
app/static/       frontend: index.html, style.css, app.js
```

## Customising
- Personality: `SYSTEM_PROMPT` in `app/config.py`
- Colours: CSS variables at the top of `app/static/style.css`
- Tools / web search / file upload: extend `stream_reply` in `app/llm.py`
- Heavy traffic: replace SQLite (`app/db.py`) with PostgreSQL
