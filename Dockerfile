# Use the official Python image as a base
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

COPY . .

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements.txt

RUN apt-get update && \
    apt-get install -y gh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN chmod +x run.py

ENTRYPOINT ["/usr/bin/bash"]

# Then:
# echo "<TOKEN>" | gh auth login --with-token
# ./run.py
