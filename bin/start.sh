#!/bin/sh

exec docker compose -f docker-compose.dev.yml run -it --build --remove-orphans devrunner
