FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ ./app
COPY entrypoint.sh .
COPY .env .
RUN chmod +x entrypoint.sh
EXPOSE 8000
ENTRYPOINT ["sh","entrypoint.sh"]
