FROM python:3.10.7
WORKDIR /app
COPY . /app

RUN pip install -r requirements.txt

ENV OPENAI_API_KEY ""

CMD ["python","app.py"]