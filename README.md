#🌱 AgriLens AI – Agricultural Crop Disease Identifier

Capstone Project – Data Science NextGen Cohort

An AI-powered crop disease diagnosis platform designed to help farmers identify crop diseases quickly using smartphone images. The system leverages Machine Learning, Cloud Computing, Geospatial Analytics, and Event-Driven Architecture to deliver near real-time disease predictions while supporting low-bandwidth and offline environments.

📌 Project Overview

AgriLens AI is an AgriTech company operating across Sub-Saharan Africa and Southeast Asia. Due to a 500% increase in image uploads, the company faces challenges with delayed disease diagnosis, infrastructure bottlenecks, and scalability issues.

This project proposes a cloud-native architecture that automates crop disease detection and reduces diagnosis time from 48–72 hours to under 5 seconds.

🎯 Business Objectives

- Reduce disease diagnosis turnaround time to less than 5 seconds.
- Achieve at least 85% F1-score on disease classification.
- Support offline-first mobile operations.
- Eliminate backend Out-of-Memory (OOM) crashes.
- Protect sensitive farm geolocation data.
- Scale automatically during seasonal demand spikes.


🚨 Problem Statement

Current diagnosis workflows depend heavily on manual agronomist reviews.

Challenges

- 48–72 hour diagnosis delay
- Frequent backend memory crashes
- Increased image upload volume
- Unreliable internet connectivity in rural areas
- Sensitive geospatial data requiring protection

Business Impact

Failure to address these challenges could result in:

- Revenue losses exceeding $1.2 million annually
- Reduced customer retention
- Contract losses with agricultural cooperatives
- Increased food insecurity for farmers


🏗️ Solution Architecture

High-Level Architecture

Farmer Mobile App
       |
       V
Google Load Balancer
       |
       V
FastAPI Gateway
       |
       +--------------------+
       |                    |
       V                    V
Signed URL Upload      Metadata Storage
       |
       V
Google Cloud Storage
       |
       V
Pub/Sub Queue
       |
       V
Image Processing Workers
       |
       V
TensorFlow Lite Inference Service
       |
       V
PostgreSQL + PostGIS
       |
       V
Notification Service
       |
       V
Farmer Receives Result


🛠 Technology Stack

Backend

- Python
- FastAPI

Machine Learning

- TensorFlow
- TensorFlow Lite
- NumPy
- Pandas
- Scikit-learn

Cloud Infrastructure

- Google Cloud Platform (GCP)
- Google Kubernetes Engine (GKE)
- Google Cloud Storage (GCS)
- Pub/Sub

Database

- PostgreSQL
- PostGIS

Mobile

- React Native
- SQLite

Monitoring

- Prometheus
- Grafana
- Google Cloud Monitoring


📂 Project Structure

agrilens-ai/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── notebooks/
│
├── src/
│   ├── api/
│   ├── preprocessing/
│   ├── training/
│   ├── inference/
│   ├── workers/
│   └── utils/
│
├── models/
│
├── tests/
│
├── deployment/
│   ├── kubernetes/
│   ├── terraform/
│   └── docker/
│
├── docs/
│
├── requirements.txt
├── Dockerfile
├── README.md
└── .gitignore


🔄 System Workflow

Step 1: Image Upload

Farmers upload crop images through a mobile application.

Step 2: Metadata Storage

The FastAPI service receives metadata and generates a signed upload URL.

Step 3: Cloud Storage

Images are uploaded directly to Google Cloud Storage.

Step 4: Event Trigger

A Pub/Sub event notifies image processing workers.

Step 5: Image Processing

Workers resize, normalize, and prepare images for inference.

Step 6: Disease Prediction

TensorFlow Lite models classify crop diseases.

Step 7: Result Storage

Predictions are stored in PostgreSQL/PostGIS.

Step 8: Farmer Notification

Results are delivered back to the farmer through the mobile application.


🤖 Machine Learning Pipeline

Dataset Sources

- Cassava Leaf Disease Dataset
- PlantVillage Dataset

Disease Classes

- Healthy
- Cassava Mosaic Disease
- Cassava Brown Streak Disease
- Leaf Blight
- Leaf Spot

Data Preprocessing

- Image resizing
- Normalization
- Data augmentation
  - Rotation
  - Flipping
  - Zooming
  - Brightness adjustment

Model Training

- Convolutional Neural Networks (CNNs)
- Transfer Learning
- Hyperparameter Optimization

Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score

Target Performance

- F1 Score ≥ 85%
- Inference Time < 2 seconds


⚡ Scalability Strategy

Event-Driven Architecture

Pub/Sub messaging decouples services and enables asynchronous processing.

Kubernetes Autoscaling

Horizontal Pod Autoscaler dynamically scales inference services based on:

- CPU utilization
- Memory utilization
- Request volume

Benefits

- Improved throughput
- Reduced latency
- High availability
- Fault tolerance


🔐 Security & Privacy

Authentication

- JWT Authentication

Encryption

- AES-256 Encryption
- HTTPS/TLS 1.3

Geospatial Privacy

- Coordinate masking
- Access controls
- Data minimization

Compliance Goals

- Privacy-by-design architecture
- Secure handling of farm location data


🌍 Offline-First Strategy

The mobile application supports operation in low-connectivity environments.

Offline Features

- Local image storage
- GPS data collection
- SQLite persistence
- Automatic synchronization when connectivity returns

Benefits

- Improved accessibility
- Reduced data loss
- Better user experience for rural farmers


📊 Monitoring & Observability

Metrics monitored include:

- API response time
- Prediction latency
- CPU utilization
- Memory usage
- Error rates
- Upload success rate

Tools

- Prometheus
- Grafana
- Google Cloud Monitoring


📈 key Performance Indicators (KPIs)

Metric| Current State| Target State
Diagnosis Time| 48–72 Hours| < 5 Seconds
Inference Latency| High| < 2 Seconds
Upload Success Rate| Unknown| 99.9%
OOM Crashes| Frequent| 0
F1 Score| N/A| ≥ 85%


🚀 Future Enhancements

- Multi-language farmer support
- Disease severity estimation
- Fertilizer recommendation engine
- Pest detection module
- Edge AI deployment on smartphones
- LLM-powered agricultural advisory assistant


👨‍💻 Author

Muhammed

Capstone Project – Data Science NextGen Cohort


📜 License

This project is developed for educational and portfolio purposes as part of the Data Science NextGen Cohort Capstone Project. 