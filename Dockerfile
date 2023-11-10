# Image mais leve do Python
FROM python:3.8-slim

# Diretório de trabalho
WORKDIR /app

# Jogando os arquivos pro diretório
COPY ./requirements.txt /app

# Instalando as dependências sem cache (instalação limpa)
RUN pip install -r requirements.txt

# Copiando os arquivos do app
COPY . .

# Expondo a porta padrão do Flask fora do Container
EXPOSE 5000

# Variável de Desenvolvimento
ENV FLASK_APP=app.py

# Rodando o servidor
CMD ["flask", "run", "--host", "0.0.0.0"]