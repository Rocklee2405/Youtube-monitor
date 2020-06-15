FROM python:3.6


COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt
COPY . /

RUN echo "Asia/SaiGon" > /etc/timezone


CMD [ "python3", "main.py" ]

