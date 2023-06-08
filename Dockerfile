# Usa la imagen de Python 3.9 como base
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el contenido de la carpeta actual al contenedor, exceptuando .storage/
COPY . /app
COPY .env /app/.env

# Instala las dependencias de Python desde requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY .data/ /app/data
# Ejecuta el paquete setup_index.py
RUN python setup_index.py

# Ejecuta el paquete bot.py en segundo plano
CMD python bot.py
