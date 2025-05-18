FROM python:3.13.3

WORKDIR /app

COPY /app .

RUN pip install -r requirements.txt

EXPOSE 8888

CMD [ "python","app.py" ]