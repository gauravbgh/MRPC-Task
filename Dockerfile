# Specifies base image and tag.
FROM python:3.8-slim

# optional
# RUN apt update && \
#     apt install --no-install-recommends -y build-essential gcc && \
#     apt clean && rm -rf /var/lib/apt/lists/*

# Sets the container working directory.
WORKDIR /root

# Copies the requirements.txt into the container to reduce network calls.
COPY requirements.txt .

# Installs additional packages.
RUN pip3 install -r requirements.txt

# Copies the trainer code to the docker image.
COPY main.py .
COPY Model_2 /Model_2

# Sets up the entry point to invoke the trainer.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
