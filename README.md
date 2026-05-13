# python_playground

A personal Python playground for learning and experimenting with:

- Rich
- Textual
- asyncio
- dataclasses
- pattern matching
- telemetry
- terminal dashboards
- AI/ML concepts
- systems programming ideas

---

# Project Structure

```text
python_playground/
├── compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
├── .gitignore
├── src/
│   ├── main.py
│   ├── nuggets/
│   │   ├── __init__.py
│   │   ├── rich_examples/
│   │   │   ├── __init__.py
│   │   │   └── signal_monitor.py
│   │   ├── asyncio_examples/
│   │   │   ├── __init__.py
│   │   │   └── workers.py
│   │   ├── data_examples/
│   │   │   ├── __init__.py
│   │   │   └── dataclasses_demo.py
│   │   └── language_examples/
│   │       ├── __init__.py
│   │       └── pattern_matching.py
│   └── utils/
│       ├── __init__.py
│       └── console.py
├── notebooks/
├── config/
└── data/
```

## Building the Container

Build and start the container:

```
docker compose up --build
```

---

## Opening a Shell

Open a shell inside the container:

```
docker compose run --rm py313 bash
```

---

## Running Examples

Run the Rich signal monitor example:

```
python -m nuggets.rich_examples.signal_monitor
```

Run the asyncio worker example:

```
python -m nuggets.asyncio_examples.workers
```

Run the dataclass example:

```
python -m nuggets.data_examples.dataclasses_demo
```

Run the pattern matching example:

```
python -m nuggets.language_examples.pattern_matching
```

---

## Python Virtual Environment

The container uses a Python virtual environment located at:

```
/workspace/.venv
```

Verify it:

```
which python
```

Expected output:

```
/workspace/.venv/bin/python
```

---

## Goals

This repository is intended to become a personal:

* Python cookbook
* telemetry sandbox
* async playground
* terminal UI lab
* AI experimentation environment
* systems programming notebook

---

## Future Topics

Potential future areas to explore:

* Textual dashboards
* Rich live telemetry
* FastAPI
* gRPC
* OpenTelemetry
* Kubernetes watchers
* NetworkX topology graphs
* SDR visualizations
* AI/ML experiments
* Agentic systems
