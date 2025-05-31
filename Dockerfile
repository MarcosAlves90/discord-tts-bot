FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir discord.py python-dotenv gtts flask pynacl

ENV PYTHONUNBUFFERED=1

CMD ["python", "bot.py"]