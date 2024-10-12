FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt \
  && rm -rf /root/.cache/pip \   
  && apt-get update \
  && apt-get install -y --no-install-recommends \   
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY . .

ENV FLASK_APP=todo_project/run.py
ENV FLASK_RUN_PORT=5000

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
