FROM python:3.11

WORKDIR /app

RUN mkdir -p /app/data

COPY . .

EXPOSE 8050

CMD ["python", "./src/main.py"]