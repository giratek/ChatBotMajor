# ChatBotMajor — Telegram Bot for Railway

## 🚀 Description
Minimal Telegram bot written in Python (aiogram) for deployment on Railway.
Uses long polling — no webhook & no domain needed.

## 🔧 Environment Variables
Set in Railway → Variables:

```
BOT_TOKEN=<your_token>
```

## 📦 Local Run

Install dependencies:

```
pip install -r requirements.txt
```

Run:

```
BOT_TOKEN=<your_token> python bot.py
```

## 🚂 Deploy to Railway

1. Push project to GitHub
2. On https://railway.app create new project
3. Select "Deploy from GitHub"
4. Open Variables → add:

```
BOT_TOKEN=your_token
```

Bot will be online in ~10 seconds.
