# FastAPI-Python-RSTUDIO
The main objective of this repository is to show how to create a Python FastAPI API, launch it thanks to Docker and consume it via RSTUDIO



# Docker: 

Nos posicionamos en la terminal dentro de la carpeta que va a tener el Docker file, en nuestro caso, a la altura 
de la carpeta de 'app'. 

Rellenamos el Dockerfile y creamos la imagen de Docker con el siguiente comando 

```
docker build -t <nombre_imagen> .
```

En mi caso, ejecuto lo siguiente en la CMD en la terminadonde estaba siguiendo este tutorial

```
docker build -t mi_primera_api_docker .
```

Me fijo que en Docker si la imagen esta creada. Bien. 


## Local-host

Seguimos en local: 

Lo corremos


```
docker run -d --name  <nombre_container> -p 80:80 <nombre_imagen>

```

En mi caso: 

```
docker run -d --name mi_api_docker  -p 80:80 mi_primera_api_docker	

```

Podremos acceder al contenido mediante: 

```

http://127.0.0.1/docs

```

Asegurate de probar con tu nombre para ver si te funciona.


## RSTUDIO

Nos posicionamos en rstudio, y abrimos un nuevo file.R

si lanzamos el siguiente comando, nos descargara la información de la API, y nos lo mostrara en pantalla:

```
install.packages(c("httr", "jsonlite"))

library(httr)
library(jsonlite)




rawToChar(GET("http://127.0.0.1/nombre?name=<TU_NOMBRE>")$content)

```