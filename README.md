# Research Reproducibility Framework (RRF)

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Python toolkit to package datasets, code, dependencies, and results for reproducible research. CLI, Docker, and optional FastAPI dashboard included.

## Problem

Scientific workflows often fail reproducibility because datasets, code, dependencies, and results are not packaged together.

## Solution

# RRF is a Python toolkit that:

- Packages code, datasets, environment, and results into reproducible bundles.

- Generates a manifest with metadata (Python versions, dependencies, timestamps).

- Provides CLI and optional dashboard for workflow execution.

- Integrates with CI/CD pipelines (GitHub Actions, GitLab, etc.) for automated reproducibility.

## Global Use

- Researchers across all disciplines

- JOSS audience

- Open science educators and labs

## Showcase Impact

- Supports open science and reproducibility

- Provides citation-ready workflows

- Enables reproducible pipelines for teaching and research

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
