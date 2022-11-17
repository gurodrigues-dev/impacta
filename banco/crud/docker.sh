# subindo container na máquina local
sudo docker run -ti --name db -p 3336:3306 -e MYSQL_PASSWORD=mysql mysql:latest

# verificando se o container está up
CONTAINER ID   IMAGE          COMMAND                  CREATED         STATUS         PORTS                                                  NAMES
51a01d6251ed   mysql:latest   "docker-entrypoint.s…"   8 minutes ago   Up 8 minutes   33060/tcp, 0.0.0.0:5000->3306/tcp, :::5000->3306/tcp   mysqlcrud

# entrando no shell 
docker exec -it mysqlcrud /bin/bash

# entrando dentro do banco de dados
$bash-4.4# mysql -uroot -p

# parando e inicializando container
docker start mysqlcrud
docker stop mysqlcrud


