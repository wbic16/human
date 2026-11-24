FROM python:3.12-slim
WORKDIR /app
COPY game/ ./game/
COPY players/ ./players/
COPY viewer/ ./viewer/
CMD ["python", "-m", "game.server"]
