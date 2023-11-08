# TP DevOps Leonardo Embon

Trabajo práctico del curso DevOps

## Instrucciones para correr en desarrollo

Clonar el proyecto:
```
$ git@github.com:lembon/tp_devops.git
```
Copiar el archivo example.env en uno nuevo llamado .env  
```
$ cp example.env .env
```
Hacer build de docker, levantar y correr migrations:
```
$ sudo docker compose -f docker-compose-dev.yml build
$ sudo docker compose -f docker-compose-dev.yml up
$ sudo docker compose -f docker-compose-dev.yml run web tp_devops_api/manage.py migrate
```
La api quedó levantada en http://localhost:8000/api/
Se puede ver la documentación e interactuar con ella en http://localhost:8000/api/docs