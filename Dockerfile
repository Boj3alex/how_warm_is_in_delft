FROM python:3.7-alpine

COPY requirements.txt /
COPY how_warm_is_in_delft.py /

RUN pip install -r /requirements.txt
COPY . /app
WORKDIR /app

CMD [ "python", "how_warm_is_in_delft.py" ]
