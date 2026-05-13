FROM python:3.13-slim

ARG USERNAME=dev
ARG UID=1000
ARG GID=1000

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    curl \
    git \
    vim \
    build-essential \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -g ${GID} ${USERNAME} \
    && useradd -m -u ${UID} -g ${GID} -s /bin/bash ${USERNAME}

USER ${USERNAME}

WORKDIR /workspace

ENV VIRTUAL_ENV=/workspace/.venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN python -m venv $VIRTUAL_ENV

COPY --chown=${USERNAME}:${USERNAME} requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

CMD ["bash"]