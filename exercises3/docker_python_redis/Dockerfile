FROM python:3.12-slim

WORKDIR /app

COPY app.py .
RUN pip install redis

CMD ["python","app.py"]
