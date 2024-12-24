# Dockerfile
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar archivos necesarios
COPY requirements.txt requirements.txt
COPY main.py main.py

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Comando para ejecutar el script principal
CMD ["python", "main.py"]