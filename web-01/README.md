# web (Dockerized Flask app)

## Build

`docker build -t demos-flask-1:latest .`

## Run

`docker run --name flask -d -p 5000:5000 demos-flask-1`

Then browse to <http://localhost:5000>

## Stop

`docker stop flask && docker rm flask`

# NGINX (for serving static content)

`docker run --name some-nginx -v /some/content:/usr/share/nginx/html:ro -d nginx`

or build a container:
 
```
FROM nginx
COPY static-html-directory /usr/share/nginx/html
```

```
docker build -t some-content-nginx .
docker run --name some-nginx -d -p 8080:80 some-content-nginx
```

Then browse to <http://localhost:8080> or http:/host-ip:8080