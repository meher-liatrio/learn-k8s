# Install metrics server:

`kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml`

edit the deployment:

`kubectl edit deployment metrics-server -n kube-system`

add 
`- --kubelet-insecure-tls`
to the args

# deliverables

- Differentiate between horizontal and vertical scaling.

> In the context of Kubernetes, horizontal auto scaling  refers to increasing the number of pods in a deployment, while vertical scaling refers to increasing the resources (CPU, memory) allocated to a pod.

- Discuss what constitutes a full monitoring solution and does Metrics Server fulfill that description?

>
    A full monitoring solution typically includes the following components:

    1. Metrics Collection: This involves gathering data about the system's performance, such as CPU usage, memory usage, network IO, disk IO, etc.

    2. Log Collection and Analysis: This involves collecting and analyzing log data from various sources to identify patterns, anomalies, or potential issues.

    3. Alerting: This involves setting up alerts based on specific conditions or thresholds. When these conditions are met, the system sends notifications to the appropriate parties.

    4. Visualization: This involves presenting the collected data in a user-friendly, visual format, often through dashboards.

    5. Tracing: This involves tracking individual requests as they traverse through various services in a system. This is particularly important in microservices architectures.

    6. Anomaly Detection: This involves using statistical methods or machine learning to detect unusual behavior in the system.

    Metrics Server in Kubernetes is a component that collects resource metrics like CPU and memory usage from nodes and pods, and exposes them via the Kubernetes API. While it's a crucial part of a monitoring solution in a Kubernetes environment, it doesn't fulfill all the requirements of a full monitoring solution by itself.

> Metrics Server primarily fulfills the "Metrics Collection" component. It doesn't handle log collection and analysis, alerting, visualization, tracing, or anomaly detection. For a complete monitoring solution in a Kubernetes environment, you would typically integrate Metrics Server with other tools like Prometheus for metrics storage and alerting, Grafana for visualization, and Fluentd or Logstash for log collection and analysis.
