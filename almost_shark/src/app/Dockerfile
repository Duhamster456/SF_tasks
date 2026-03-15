FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

EXPOSE 1234
CMD ["gunicorn", "--bind", "0.0.0.0:1234", "app:app"]