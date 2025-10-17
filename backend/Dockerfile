FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ADD . .

RUN uv sync --locked

EXPOSE 5174
RUN uv pip install sanic tortoise tortoise-orm aiomysql asyncmy
CMD ["/bin/uv", "run", "main.py"]