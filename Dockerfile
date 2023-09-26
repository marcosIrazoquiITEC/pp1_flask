FROM python:3.10.12

# Copia todo lo del directorio en el contenedor
COPY . /aplicacion

# Setea el directorio de trabajo en el contenedor
WORKDIR /aplicacion

# Corre comandos
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expone puerto
EXPOSE 5005

ENTRYPOINT [ "python" ]

CMD [ "app/__init__.py" ]