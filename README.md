# realShit
Create a Django project in Docker

## How to run the container :whale2:

> sudo command is required

1. Build the DockerFile

```
sudo docker build . 

```

1. Run docker-compose

```
sudo docker-compose build 

```

1. Run composer up

```
sudo docker-compose up 

```

```
sudo docker ps

```

```
sudo docker exec <container_name> <python instrucction> 

```

```
sudo chown -R $USER:$USER .

```

```python
docker-compose exec movies pytest --cov-report html --cov tests/movies
```
