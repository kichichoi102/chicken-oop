FROM python:3.9-slim as compiler
ENV PYTHONUNBUFFERED 1

WORKDIR /

RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./requirements.txt /requirements.txt
RUN pip install -Ur requirements.txt

# Add tests
COPY farm /farm
COPY ./tests /tests
RUN pytest /tests

FROM python:3.9-slim as runner
WORKDIR /
COPY --from=compiler /opt/venv /opt/venv

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /
CMD ["python3", "main.py"]