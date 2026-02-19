# CloudSense IoT Real-Time Simulation

A scalable cloud-based IoT ingestion system using:

- AWS API Gateway
- AWS Lambda
- DynamoDB (real-time storage)
- S3 (historical storage)
- Python-based multi-sensor simulator

## Architecture

Sensor Simulator → API Gateway → Lambda → DynamoDB + S3

## Features

- Real-time multi-sensor simulation
- Serverless ingestion pipeline
- Automatic JSON logging to S3
- Scalable DynamoDB storage

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run single sensor:
   python auto_sensor.py

3. Run multi-sensor simulation:
   python multi_sensor.py
