FROM python:3.8.10
ENV POETRY_VERSION=1.1.13
RUN pip install "poetry==$POETRY_VERSION"
#RUN curl -sSL https://install.python-poetry.org | python3 - --version "1.1.13"
ENV PATH="/root/.local/bin:$PATH"
WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-dev --no-root
COPY . app/
RUN poetry config virtualenvs.in-project true --local
RUN poetry install --no-dev

CMD ["poetry", "run", "python", "main.py"]
