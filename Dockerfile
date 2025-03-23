FROM python:3.9

WORKDIR /app

COPY log_anomaly_detection.py /app
RUN pip install pandas scikit-learn boto3

CMD ["python", "log_anomaly_detection.py"]   
