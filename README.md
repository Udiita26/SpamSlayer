# 📧 SpamSlayer

**SpamSlayer** is a Python tool that connects to your Gmail and checks if your recent emails are spam or not using a trained ML model. It's smart enough to catch spammy messages like Snapchat alerts too!

## 🔍 What It Does

- Connects to your Gmail using OAuth (secure login)
- Fetches latest emails (subject + body)
- Uses a custom-trained model to label them as 🚫 Spam or 📬 Not Spam

## 🧠 Built With

- Python + scikit-learn
- Gmail API
- OAuth2 + dotenv

## 📁 What's in This Repo

You'll find all the important project files here:

- `classify_emails.py`, `fetch_emails.py`, `train_model.py` – main code
- `spam_classifier.pkl` – the trained ML model

> ❗ **Note:**  
> This repo does **not** include your `credentials.json`, `token.json`, or your own `.env`. You’ll need to set those up yourself for privacy and security.
