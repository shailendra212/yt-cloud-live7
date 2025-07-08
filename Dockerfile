FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install ffmpeg-python

COPY main.py /app/main.py

CMD ["python", "/app/main.py"]
