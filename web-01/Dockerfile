FROM ubuntu:latest
MAINTAINER Brian Schlining "brian@mbari.org"

RUN apt-get update -y \
    && apt-get install -y python-pip python-dev build-essential

COPY . /app
WORKDIR /app
RUN pip install  -r requirements.txt
ENTRYPOINT [ "python" ]

CMD ["app.py"]