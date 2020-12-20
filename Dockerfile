FROM python:3.8

WORKDIR /app
COPY src .
RUN pip3 install -r requirements.txt

CMD ["/bin/sh", "-c", "python manage.py migrate && python -u manage.py runscript main"]