FROM python:3.5

ADD . /

RUN pip install -r requirements.txt

ENTRYPOINT ["python","main.py"]