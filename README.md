# Research Reproducibility Framework (RRF)

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Python toolkit to package datasets, code, dependencies, and results for reproducible research. CLI, Docker, and optional FastAPI dashboard included.

## Quickstart

```bash
pip install -r requirements.txt
python -m rrf.packager --input ./my-project --output ./bundle.zip
python -m rrf.runner --bundle ./bundle.zip --execute
```

## Docker

```bash
docker build -t rrf_tool .
docker run -v $(pwd)/data:/data rrf_tool
```

## Tests
```bash
pytest
```

## JOSS Submission
JOSS-ready paper in `paper/paper.md` and bibliography `paper/paper.bib`.
