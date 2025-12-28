FROM python:3.11-slim
WORKDIR /app
COPY ../requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
COPY ../data ../data
RUN mkdir -p /app/data
EXPOSE 3018
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=3018"]
