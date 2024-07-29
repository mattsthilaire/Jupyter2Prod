FROM python:3.9
RUN mkdir app
WORKDIR /app
COPY /pyproject.toml poetry.lock /app/
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root
COPY . .
CMD ["fastapi", "run", "src/main.py", "--port", "80"]
#CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "src.main:app", "--bind", "0.0.0.0:8000"]