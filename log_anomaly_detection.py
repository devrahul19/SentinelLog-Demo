import boto3
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

# AWS CloudWatch Config
log_group = "SentinelLog-Demo"
log_stream = "TestStream"
client = boto3.client('logs', region_name="us-east-1")  # Change region if needed

# Fetch logs
response = client.get_log_events(logGroupName=log_group, logStreamName=log_stream)
logs = [event["message"] for event in response["events"]]

# Convert logs to numerical data (fake CPU usage example)
data = [float(log.split()[-1].replace('%', '')) if '%' in log else np.random.randint(10, 90) for log in logs]
df = pd.DataFrame(data, columns=["CPU_Usage"])

# Train Isolation Forest Model
model = IsolationForest(contamination=0.1)
df["Anomaly"] = model.fit_predict(df[["CPU_Usage"]])

# Show anomalies
anomalies = df[df["Anomaly"] == -1]
print("Anomalies detected:", anomalies)