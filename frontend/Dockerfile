FROM oven/bun:latest

WORKDIR /app

COPY package.json .

RUN bun install --no-fund --no-progress

COPY . .

EXPOSE 5173

CMD ["bun", "run", "dev"]