ARG python_image_v="python:3.10-buster"

FROM ${python_image_v}

ENV DEBIAN_FRONTEND=noninteractive

SHELL ["/bin/bash", "-c"]

RUN apt update && apt install -y \
    git \
    curl \
    libportaudio2 \
    && rm -rf /var/lib/apt/lists

ENV PATH /etc/poetry/bin:$PATH

RUN source ~/.bashrc \
    && curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -

ENV POETRY_VIRTUALENVS_CREATE=false
