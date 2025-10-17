FROM oven/bun:latest

WORKDIR /app

COPY package.json .

RUN bun install --no-fund --no-progress

# 复制项目所有文件
COPY . .

EXPOSE 5173

CMD ["bun", "run", "dev"]