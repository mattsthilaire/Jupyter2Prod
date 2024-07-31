# This works locally for gunicorn and poetry
FROM python:3.10 as python-base
RUN mkdir app
WORKDIR  /app
#COPY /pyproject.toml /app
#RUN pip install poetry
#RUN poetry config virtualenvs.create false
#RUN poetry install
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "src.main:app", "--bind", "0.0.0.0:8000"]

### The below is for local debugging with fastapi
#FROM python:3.9
#RUN mkdir app
#WORKDIR /app
#COPY /pyproject.toml poetry.lock /app/
#RUN pip install poetry
#RUN poetry config virtualenvs.create false
#RUN poetry install --no-root
#COPY . .
#CMD ["fastapi", "run", "src/main.py", "--port", "80"]