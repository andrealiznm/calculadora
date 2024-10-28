# Usando una imagen base de Python
FROM python:3.9-slim

# Directorio de trabajo en el contenedor
WORKDIR /app

# Copiando los archivos necesarios
COPY calculadora.py /app/
COPY requirements.txt /app/

# Pasando las variables de entorno para calcualdora.py
ENV OPERACION=1
ENV NUM1=10
ENV NUM2=5

# Instalando las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Ejecucion de la aplicación
CMD ["python", "calculadora.py"]
