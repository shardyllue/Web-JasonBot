FROM python:3.11

WORKDIR /app

COPY . .

RUN pip3 install --upgrade setuptools
RUN pip3 install poetry
RUN poetry shell
RUN poetry update

RUN chmod 755 .

CMD [ "uvicorn", "app:app"]