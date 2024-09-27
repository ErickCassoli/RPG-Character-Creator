# Usando imagem oficial do Python
FROM python:3.9-slim

# Instalar dependências do sistema necessárias para compilar psycopg2
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Definindo diretório de trabalho
WORKDIR /app

# Copiar o requirements.txt e instalar as dependências
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação
COPY . .

# Expondo a porta da aplicação FastAPI
EXPOSE 8000

# Comando para iniciar o servidor FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
