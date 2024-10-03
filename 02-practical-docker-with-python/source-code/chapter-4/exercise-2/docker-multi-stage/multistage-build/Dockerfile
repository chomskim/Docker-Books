FROM python:3 AS python-base

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

FROM python:3.9-alpine

COPY --from=python-base /root/.cache /root/.cache

COPY --from=python-base /app/requirements.txt .

RUN pip install -r requirements.txt && rm -rf /root/.cache
