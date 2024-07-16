FROM python:3.9

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN python -m pip install --upgrade pip

COPY ./app /app

RUN pip install -r requirements.txt

RUN apt-get install -y libgl1
RUN apt-get install sshpass
RUN apt-get install -y liblzma-dev