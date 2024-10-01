# The Simulator

This python project is the simulator core, it uses SimPy to model the simulation.

## How to run

Make sure to install python 3.10 and then run.

```
poetry env use 3.10
poetry install
```

```
poetry run fastapi dev src/simulator/main.py --host 127.0.0.1 --port 8000
```
