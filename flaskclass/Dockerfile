FROM python:alpine3.6 

RUN apk add --update \
    bash

COPY requirements.txt . 

RUN pip install -r requirements.txt 

COPY api.py .

EXPOSE 5000 

COPY entrypoint.sh .
ENTRYPOINT ["./entrypoint.sh"]