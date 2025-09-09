# version av Dockerfile-syntax som används-python alpine container
FROM python:3.10-alpine AS builder

#Ställer in /flaskapp som arbetskatalog inuti containern.Alla COPY och RUN-kommandon sker i /flaskapp
WORKDIR /flaskapp


COPY requirements.txt .

RUN pip3 install --no-cache-dir -r requirements.txt

#Kopierar hela projektmappen in i /app
COPY . /flaskapp

#anger att alla kommandon startas med python3
ENTRYPOINT ["python3"]

#standardfil som körs när containern startar
CMD ["app.py"]



