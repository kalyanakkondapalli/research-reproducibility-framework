FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml ./
RUN pip install --upgrade pip && pip install -r requirements.txt || pip install typer pyyaml fastapi uvicorn pytest
COPY . .
CMD ["python", "-m", "rrf.packager", "--input", "/data/project", "--output", "/data/bundle.zip"]
