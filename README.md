# AI Moderator

ИИ Модератор дискорд на основе G4F

# Установка

```bash
py -m pip install -r requirements.txt
# или
python3 -m pip install -r requirements.txt
```

Настройте .env по примеру:

```env
TOKEN=YOUR_TOKEN
ADMIN_IDS=ID1,ID2
```

Смените правила по необходимости в utils/ask_gpt.py в переменной system_prompt
Также смените модель если нужно

# Запуск

```bash
py main.py
# или
python3 main.py
```
