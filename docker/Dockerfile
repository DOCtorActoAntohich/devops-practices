FROM python:3.10
WORKDIR /app


EXPOSE 8000


# Environment.
COPY ./docker/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r ./requirements.txt


# Executables.
COPY ./app_python ./app_python


# root evil.
RUN addgroup --system cats && adduser --system --ingroup cats floppa
USER floppa


# RUN
ENTRYPOINT gunicorn -k uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 app_python.main:app
