# BOT SENCILLO DE TELEGRAM USANDO LA API DE TELEGRAM Y LLAMA INDEX CON GPT

# CONFIGURACIÓN 

## INSTALANDO DEPENDENCIAS

Para este bot hemos usado dos librerias de python python-telegram y llama-index las puedes instalar desde el archivo de requirements
aunque te recomiendo que crees un entorno para esto:

```
pip install -r requirements.txt
```

## GENERANDO LAS KEYS

Necesitas un API-KEY de bots de telegram para esto desde el propio telegram habla con BotFather 

En segundo lugar necesitas un API-KEY  de GPT entra en la página de chat.openai.com y genera una

En el caso de que estes desplegando un bot ya existente pidele a quien corresponda que te de las api keys del bot.

estas keys y la ruta del directorio que queremos usar como índice lo dejaremos en un archivo .env con esta pinta:

```
OPENAI_API_KEY = key-super-secreta-de-openai
TELEGRAM_BOT_API_KEY = key-del-bot-del-telegram
DATA_FOLDER = ruta-de-la-carpeta
```

# GENERANDO EL INDICE

Este bot va a usar GPT enriquecido para contestar a nuestras preguntas para ello lo que hemos hecho es aprovechar
la libreria llama-index la cual por medio del archivo setup_index.py nos ayuda a generar los indices correspondientes
al contenido de los archivos de la carpeta que le hayamos indicado en el archivo .env

```
python setup_index.py
```

# ACTIVANDO EL BOT

Ya estan los preparativos listos solo tenemos que lanzar el bot, este es un ejemplo muy sencillo pero nos sirve de plantilla para
añadirle toda la funcionalidad que necesitemos.

```
python bot.py
```

# SI LO QUIERES MONTAR CON DOCKER

Si quieres montar el bot desde una imagen de docker he preparado un Dockerfile sencillo para 
poder hacerlo desde dentro de un contenedor en lugar de en tu propia máquina, nota para esta version los datos que queremos indexar 
deberemos dejarlos enla carpeta data (lo he hecho así por simplicidad y falta de tiempo se podria configurar tambien).

creando el contenedor:

```
docker build -t mi_bot_container .
```

ejecutando el contenedor con el bot

```
docker run -d --name mi_bot mi_bot_container

```

