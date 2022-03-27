FROM python:3.10

WORKDIR /usr/src/app

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
