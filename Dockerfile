FROM python:3.10.5-slim-buster




RUN apt-get update

CMD ["python3", /bot]
