# Build step
FROM python:3.10-slim as build

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY microservice_audio_storage.py .

# Test step
FROM build as test

COPY test_microservice_audio_storage.py .
RUN pytest --cov=microservice_audio_storage --cov-report html test_microservice_audio_storage.py

# Production step
FROM python:3.10-slim as production

WORKDIR /app

COPY --from=build /app/microservice_audio_storage.py .

COPY production_requirements.txt .
RUN pip install --no-cache-dir -r production_requirements.txt

EXPOSE 5000

CMD ["python3", "microservice_audio_storage.py"]
