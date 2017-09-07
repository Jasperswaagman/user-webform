FROM python:alpine3.6

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
COPY app/ /app
EXPOSE 5000
CMD ["python","main.py"] 